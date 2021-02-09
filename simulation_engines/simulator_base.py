class base_simulator():

    def __init__(self, bodies):
        self.current_bodies_state = bodies
        self.G = 6.67430 * 10**(-11)
    
    def update(self,sim_time_delta):
        '''
        Should simulate forward sim_time_delta seconds.
        The simulator class should only ever store the most up to date data.
        Any data storage should be handled outside of this class
        '''
        raise NotImplementedError

    def getCurrentState(self):
        raise NotImplementedError