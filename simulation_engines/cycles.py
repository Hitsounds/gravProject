from .simulator_base import base_simulator
import numpy as np

class cycles(base_simulator):

    def __init__(self, bodies):
        #Initalise base class with bodies table
        super().__init__(bodies)
        
    def _forceBetweenTwoBodies(self, body1_index, body2_index):
        '''Takes in 2 indexes and returns the force vector due to gravity
        between the two bodies
        '''
        #Masses as float kilograms
        b1_mass = self.current_bodies_state[body1_index]["mass"]
        b2_mass = self.current_bodies_state[body2_index]["mass"]
        #Positions as numpy vectors
        b1_pos = self.current_bodies_state[body1_index]["pos"]
        b2_pos = self.current_bodies_state[body2_index]["pos"]
        #vector between positions
        delta_pos = b1_pos - b2_pos
        #Calculate magnitude of force
        force_mag = -self.G * (b1_mass*b2_mass)/(np.linalg.norm(delta_pos)**2)
        #Times by unit vector to get force as a vector
        force_vector = force_mag * (delta_pos/np.linalg.norm(delta_pos))
        return force_vector
    
    def _calculateForceOnBodies(self):
        '''
        Calculates the resultant forces on each body in the system
        '''
        output = [np.array([0.0,0.0]) for _ in range(len(self.current_bodies_state))]
        for i in range(len(self.current_bodies_state)):
            #for every body in system
            for j in range(i+1,len(self.current_bodies_state)):
                #for every body which still needs a force to be calculated
                force = self._forceBetweenTwoBodies(i,j)
                #forces are equal but opposite
                output[i] = output[i] + force
                output[j] = output[j] - force
        return output

    def _calculateAccelerationOnBodies(self):
        '''
        Calculates the resultant acceleration on each body in the system
        '''
        accelerations = self._calculateForceOnBodies()
        for i in range(len(self.current_bodies_state)):
            accelerations[i] = accelerations[i] / self.current_bodies_state[i]["mass"]
        return accelerations

    def update(self, sim_time_delta):
        '''
        Update function to simulate forward sim_time_delta seconds
        '''
        accelerations = self._calculateAccelerationOnBodies()
        #Calculate offset to keep centre body at 0,0 and 0 velocity
        pos_offset = self.current_bodies_state[0]["pos"] + (self.current_bodies_state[0]["vel"]*sim_time_delta) + (0.5*accelerations[0]*(sim_time_delta**2))
        vel_offset = self.current_bodies_state[0]["vel"] + accelerations[0]*sim_time_delta
        for i in range(len(self.current_bodies_state)):
            #Using suvat s = ut + 0.5at^2 to calculate new positions
            self.current_bodies_state[i]["pos"] = self.current_bodies_state[i]["pos"] + ((self.current_bodies_state[i]["vel"]*sim_time_delta) + (0.5*accelerations[i]*(sim_time_delta**2))) - pos_offset
            self.current_bodies_state[i]["vel"] = (self.current_bodies_state[i]["vel"] +  accelerations[i]*sim_time_delta) - vel_offset
        return self.current_bodies_state
        
    def getCurrentState(self):
        '''
        Returns current state of simulation
        '''
        return self.current_bodies_state