import rclpy
from rclpy.node import Node
from std_msgs.msg import Float32
import math

class TrigPublisher(Node):
    def __init__(self):
        super().__init__('trig_publisher')
        self.publisher_sin = self.create_publisher(Float32, 'sin_wave', 10)
        self.publisher_cos = self.create_publisher(Float32, 'cos_wave', 10)
        self.timer = self.create_timer(0.1, self.timer_callback)
        self.t = 0.0

    def timer_callback(self):
        sin_msg = Float32()
        cos_msg = Float32()
        sin_msg.data = math.sin(self.t)
        cos_msg.data = math.cos(self.t)
        self.publisher_sin.publish(sin_msg)
        self.publisher_cos.publish(cos_msg)
        self.get_logger().info(f'Sin: {sin_msg.data:.2f}, Cos: {cos_msg.data:.2f}')
        self.t += 0.1

def main(args=None):
    rclpy.init(args=args)
    node = TrigPublisher()
    rclpy.spin(node)
    node.destroy_node()
    rclpy.shutdown()

if __name__ == '__main__':
    main()