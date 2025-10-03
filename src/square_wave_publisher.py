import rclpy
from rclpy.node import Node
from std_msgs.msg import Float32

class SquareWavePublisher(Node):
    def __init__(self):
        super().__init__('square_wave_publisher')
        self.publisher_ = self.create_publisher(Float32, 'square_wave', 10)

        self.declare_parameter('frequency', 1.0)   # Hz
        self.declare_parameter('amplitude', 1.0)
        self.declare_parameter('duty', 0.5)        # kitöltési tényező
        self.declare_parameter('rate', 50.0)       # mintavétel Hz

        self.freq = self.get_parameter('frequency').get_parameter_value().double_value
        self.amp = self.get_parameter('amplitude').get_parameter_value().double_value
        self.duty = self.get_parameter('duty').get_parameter_value().double_value
        self.rate = self.get_parameter('rate').get_parameter_value().double_value

        self.t = 0.0
        self.dt = 1.0 / self.rate
        self.timer = self.create_timer(self.dt, self.timer_callback)

    def timer_callback(self):
        phase = (self.t * self.freq) % 1.0
        value = self.amp if phase < self.duty else -self.amp
        msg = Float32()
        msg.data = float(value)
        self.publisher_.publish(msg)
        self.t += self.dt

def main(args=None):
    rclpy.init(args=args)
    node = SquareWavePublisher()
    rclpy.spin(node)
    node.destroy_node()
    rclpy.shutdown()

if __name__ == '__main__':
    main()
