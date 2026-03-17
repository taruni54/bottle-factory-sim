#!/usr/bin/env python3

import rclpy
from rclpy.node import Node
from rclpy.publisher import Publisher
from std_msgs.msg import Float64, Int32
import time

class FactoryController(Node):
    def __init__(self):
        super().__init__('factory_controller')
        self.station1_cycle_time = 4
        self.station2_cycle_time = 7
        self.station3_cycle_time = 5
        
        self.throughput_publisher = self.create_publisher(Float64, 'throughput', 10)
        self.queue_depth_publisher = self.create_publisher(Int32, 'queue_depth', 10)
        self.oee_publisher = self.create_publisher(Float64, 'oee', 10)
        self.utilization_publisher = self.create_publisher(Float64, 'utilization', 10)

        self.current_queue_depth = 0
        self.total_produced = 0
        
        self.timer = self.create_timer(1.0, self.publish_metrics)

    def publish_metrics(self):
        # Simulate KPIs
        cycle_times = [self.station1_cycle_time, self.station2_cycle_time, self.station3_cycle_time]
        min_cycle_time = min(cycle_times)
        
        self.current_queue_depth += 1  # for the sake of simulation
        self.total_produced += (1 / min_cycle_time)

        throughput = self.total_produced
        oee = (throughput / (self.current_queue_depth + 1)) * 100  # simple OEE calculation
        utilization = (1 / min(cycle_times)) * 100  # Utilization based on minimum cycle time

        self.throughput_publisher.publish(throughput)
        self.queue_depth_publisher.publish(self.current_queue_depth)
        self.oee_publisher.publish(oee)
        self.utilization_publisher.publish(utilization)

def main(args=None):
    rclpy.init(args=args)
    factory_controller = FactoryController()
    rclpy.spin(factory_controller)
    factory_controller.destroy_node()
    rclpy.shutdown()

if __name__ == '__main__':
    main()