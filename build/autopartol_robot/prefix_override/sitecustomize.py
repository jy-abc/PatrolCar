import sys
if sys.prefix == '/usr':
    sys.real_prefix = sys.prefix
    sys.prefix = sys.exec_prefix = '/home/jy/vscode/ros2_learning/chapter7/chapter7_ws/install/autopartol_robot'
