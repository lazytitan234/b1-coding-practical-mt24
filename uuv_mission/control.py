class PDController:
    def __init__(self, kp: float = 0.15, kd: float = 0.6):
        self.kp = kp
        self.kd = kd
        self.reset()

    def reset(self) -> None:
        self.prev_error = 0.0

    def get_action(self, reference: float, observation: float) -> float:
        error = reference - observation
        action = self.kp * error + self.kd * (error - self.prev_error)
        self.prev_error = error
        return action