import rclpy
from rclpy.node import Node
from std_msgs.msg import Float32
import math

class TrigWavePublisher(Node):
    def __init__(self):
        super().__init__('trig_wave_publisher')

        # Két topic: /sin_wave és /cos_wave
        self.sin_pub = self.create_publisher(Float32, 'sin_wave', 10)
        self.cos_pub = self.create_publisher(Float32, 'cos_wave', 10)

        # Paraméterek
        self.declare_parameter('frequency', 1.0)  # Hz
        self.declare_parameter('amplitude', 1.0)
        self.declare_parameter('rate', 50.0)      # mintavétel Hz

        self.freq = self.get_parameter('frequency').value
        self.amp = self.get_parameter('amplitude').value
        self.rate = self.get_parameter('rate').value

        self.t = 0.0
        self.dt = 1.0 / self.rate

        self.timer = self.create_timer(self.dt, self.timer_callback)
        self.get_logger().info(
            f'Started trig_wave_publisher with f={self.freq}Hz, A={self.amp}, rate={self.rate}Hz'
        )

    def timer_callback(self):
        # Idő növelése
        self.t += self.dt
        omega = 2.0 * math.pi * self.freq * self.t

        sin_val = self.amp * math.sin(omega)
        cos_val = self.amp * math.cos(omega)

        # Publikálás
        self.sin_pub.publish(Float32(data=sin_val))
        self.cos_pub.publish(Float32(data=cos_val))

def main(args=None):
    rclpy.init(args=args)
    node = TrigWavePublisher()
    rclpy.spin(node)
    node.destroy_node()
    rclpy.shutdown()

if __name__ == '__main__':
    main()
