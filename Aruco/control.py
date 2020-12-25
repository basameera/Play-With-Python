class PID:
    def __init__(self, kp=0, kd=0, ki=0, set_point=0, offset=None):
        self.kp = kp
        self.kd = kd
        self.ki = ki

        self.set_point = set_point
        self.offset = offset

    def p_ctrl(self, feedback):
        error = feedback - self.set_point
        output = self.kp * error
        return output


if __name__ == "__main__":
    pass
