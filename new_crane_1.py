#Do not use this one, use new_crane.py instead, it is the one that has been tested and improved


from asyncua.sync import Client
from asyncua import ua
import datetime 

class Crane(object): 
    """Definition of Ilmatar Crane interface through OPC UA."""

    def __init__(self, clientaddress) -> None:
        self.x = 1
        self.client = Client(clientaddress)
        self.client.connect() 

        #NS = "ns=" + str(self.client.get_namespace_index("AIIC"))
        NS = "ns=5"

        # Watchdog
        self._node_watchdog = self.client.get_node(
            NS + ";s=DX_Custom_V.Controls.Watchdog")
        
        # Accescode
        self._node_access_code = self.client.get_node(
            NS + ";s=DX_Custom_V.Controls.AccessCode")

        # Crane Direction booleans
        self._node_hoist_up = self.client.get_node(
            NS + ";s=DX_Custom_V.Controls.Hoist.Up")
        self._node_hoist_down = self.client.get_node(
            NS + ";s=DX_Custom_V.Controls.Hoist.Down")
        self._node_trolley_forward = self.client.get_node(
            NS + ";s=DX_Custom_V.Controls.Trolley.Forward")
        self._node_trolley_backward = self.client.get_node(
            NS + ";s=DX_Custom_V.Controls.Trolley.Backward")
        self._node_bridge_forward = self.client.get_node(
            NS + ";s=DX_Custom_V.Controls.Bridge.Forward")
        self._node_bridge_backward = self.client.get_node(
            NS + ";s=DX_Custom_V.Controls.Bridge.Backward")

        # Crane speed
        self._node_hoist_speed = self.client.get_node(
            NS + ";s=DX_Custom_V.Controls.Hoist.Speed")
        self._node_trolley_speed = self.client.get_node(
            NS + ";s=DX_Custom_V.Controls.Trolley.Speed")
        self._node_bridge_speed = self.client.get_node(
            NS + ";s=DX_Custom_V.Controls.Bridge.Speed")

        # Position
        self._node_hoist_position_mm = self.client.get_node(
            NS + ";s=DX_Custom_V.Status.Hoist.Position.Position_mm")
        self._node_trolley_position_mm = self.client.get_node(
            NS + ";s=DX_Custom_V.Status.Trolley.Position.Position_mm")
        self._node_bridge_position_mm = self.client.get_node(
            NS + ";s=DX_Custom_V.Status.Bridge.Position.Position_mm")
        self._node_hoist_position_m = self.client.get_node(
            NS + ";s=DX_Custom_V.Status.Hoist.Position.Position_m")
        self._node_trolley_position_m = self.client.get_node(
            NS + ";s=DX_Custom_V.Status.Trolley.Position.Position_m")
        self._node_bridge_position_m = self.client.get_node(
            NS + ";s=DX_Custom_V.Status.Bridge.Position.Position_m")

        
        # Loads
        self._node_hoist_current_load = self.client.get_node(
            NS + ";s=DX_Custom_V.Status.Hoist.Load.Load_t")
        self._node_hoist_current_tared_load = self.client.get_node(
            NS + ";s=DX_Custom_V.Status.Hoist.Load.TaredLoad_t")

        # Datetime
        self._node_datime_year = self.client.get_node(
            NS + ";s=DX_Custom_V.Datetime.Year")
        self._node_datime_month = self.client.get_node(
            NS + ";s=DX_Custom_V.Datetime.Month")
        self._node_datime_day = self.client.get_node(
            NS + ";s=DX_Custom_V.Datetime.Day")
        self._node_datime_hour = self.client.get_node(
            NS + ";s=DX_Custom_V.Datetime.Hour")
        self._node_datime_minute = self.client.get_node(
            NS + ";s=DX_Custom_V.Datetime.Minute")
        self._node_datime_second = self.client.get_node(
            NS + ";s=DX_Custom_V.Datetime.Second")
        self._node_datime_millisecond = self.client.get_node(
            NS + ";s=DX_Custom_V.Datetime.Millisecond")

        # Control signal status

        # Not currently used
        self._node_trolley_direction_forward_request = self.client.get_node(
            NS + ";s=DX_Custom_V.Status.Trolley.ControlSignals.Direction1_Request")
        self._node_trolley_direction_backwards_request = self.client.get_node(
            NS + ";s=DX_Custom_V.Status.Trolley.ControlSignals.Direction2_Request")
        self._node_trolley_speed_request = self.client.get_node(
            NS + ";s=DX_Custom_V.Status.Trolley.ControlSignals.SpeedRequest")
        self._node_trolley_speed_feedback = self.client.get_node(
            NS + ";s=DX_Custom_V.Status.Trolley.ControlSignals.SpeedFeedback")
        self._node_trolley_speed_feedback_mmin = self.client.get_node(
            NS + ";s=DX_Custom_V.Status.Trolley.ControlSignals.SpeedFeedback_mmin")


        # Not currently used
        self._node_bridge_direction_forward_request = self.client.get_node(
            NS + ";s=DX_Custom_V.Status.Bridge.ControlSignals.Direction1_Request")
        self._node_bridge_direction_backward_request = self.client.get_node(
            NS + ";s=DX_Custom_V.Status.Bridge.ControlSignals.Direction2_Request")
        self._node_bridge_speed_request = self.client.get_node(
            NS + ";s=DX_Custom_V.Status.Bridge.ControlSignals.SpeedRequest")
        self._node_brige_speed_feedback = self.client.get_node(
            NS + ";s=DX_Custom_V.Status.Bridge.ControlSignals.SpeedFeedback")
        self._node_brige_speed_feedback_mmin = self.client.get_node(
            NS + ";s=DX_Custom_V.Status.Bridge.ControlSignals.SpeedFeedback_mmin")


        # Not currently used
        self._node_hoist_direction_up_request = self.client.get_node(
            NS + ";s=DX_Custom_V.Status.Hoist.ControlSignals.Direction1_Request")
        self._node_hoist_direction_down_request = self.client.get_node(
            NS + ";s=DX_Custom_V.Status.Hoist.ControlSignals.Direction2_Request")
        self._node_hoist_speed_request = self.client.get_node(
            NS + ";s=DX_Custom_V.Status.Hoist.ControlSignals.SpeedRequest")
        self._node_hoist_speed_feedback = self.client.get_node(
            NS + ";s=DX_Custom_V.Status.Hoist.ControlSignals.SpeedFeedback")
        self._node_hoist_speed_feedback_mmin = self.client.get_node(
            NS + ";s=DX_Custom_V.Status.Hoist.ControlSignals.SpeedFeedback_mmin")


        self.bridge_last_zeroed = self.get_motorcontroller_bridge_value()
        self.trolley_last_zeroed = self.get_motorcontroller_trolley_value()
        self.hoist_last_zeroed = self.get_motorcontroller_hoist_value()

        self._watchdog_value = self.get_watchdog()

        # Will be initialized in set_moving_height
        self.hoist_moving_height = None

        # Will be initialized in set_target_current_position later in __init__
        self.trolley_target = None
        self.bridge_target = None
        self.hoist_target = None

        self.set_target_current_position()


    """Functions related to connecting to opcua server"""

    def connect(self):
        """Connect to the OPC UA Server."""
        self.client.connect()


    def disconnect(self):
        """Disconnect from OPC UA Server."""
        self.client.disconnect()


    """Functions related to watchdog"""

    def get_watchdog(self):
        """Get Watchdog value."""
        return self._node_watchdog.read_value()


    # Not working
    def set_watchdog(self, watchdog_value):
        """Set Watchdog to number x."""
        self._node_watchdog.write_value(ua.DataValue(ua.Variant(watchdog_value, ua.VariantType.Int16)))


    def increment_watchdog(self):
        """Increment Watchdog by 1."""
        print(self._watchdog_value)
        self._watchdog_value = (self._watchdog_value % 30000) + 1
        self.set_watchdog(self._watchdog_value)

    #Not tested if works
    #def reset_watchdog(self): 
     #   """Reset the watchdog to zero"""
      #  self._watchdog_value = 0 

    
    
        """Functions related to accesscode"""

    def get_accesscode(self):
        """Get AccessCode value."""
        return self._node_access_code.read_value()


    def set_accesscode(self, accesscode):
        """Set AccessCode to number x."""
        self._node_access_code.write_value(ua.DataValue(ua.Variant(accesscode, ua.VariantType.Int32)))

    
    """Functions to get position for crane"""

    def get_trolley_position_absolute(self):
        """Get absolute position for Trolley in mm (laser)."""
        return self._node_trolley_position_m.read_value() * 1000


    def get_motorcontroller_trolley_value(self):
        """Get value from motorcontroller for Trolley."""
        return self._node_trolley_position_mm.read_value()


    def get_bridge_position_absolute(self):
        """Get absolute position for Bridge in mm (laser)."""
        return self._node_bridge_position_m.read_value() * 1000


    def get_motorcontroller_bridge_value(self):
        """Get value from motorcontroller for Bridge."""
        return self._node_bridge_position_mm.read_value()


    def get_hoist_position_absolute(self):
        """ Get absolute position for Hoist in mm """
        return self._node_hoist_position_m.read_value() * 1000


    def get_motorcontroller_hoist_value(self):
        """Get value from motorcontroller for Hoist."""
        return self._node_hoist_position_mm.read_value()


    def get_coordinates_absolute(self):
        """Get absolute position for Bridge,Trolley and Hoist in mm (laser)."""
        return(self._node_bridge_position_mm.read_value(),
               self._node_trolley_position_mm.read_value(),
               self._node_hoist_position_mm.read_value())


    def get_motorcontroller_all(self):
        """Get all values from motorcontroller, Bridge, Trolley, Hoist."""
        return(self.get_motorcontroller_bridge_value(),
               self.get_motorcontroller_trolley_value(),
               self.get_motorcontroller_hoist_value())


    """Functions to get positions with timestamp for bridge and trolley"""

    def get_motocontroller_bridge_value_with_timestamp(self):
        """Get value from motorcontroller for Bridge with timestamp."""
        data = self._node_bridge_position_mm.read_data_value()
        return (data.Value.Value, data.SourceTimestamp.timestamp())


    def get_motocontroller_trolley_value_with_timestamp(self):
        """Get value from motorcontroller for trolley with timestamp."""
        data = self._node_trolley_position_mm.read_data_value()
        return (data.Value.Value, data.SourceTimestamp.timestamp())


    """Functions to get speed with timestamp for crane"""

    def get_speed_bridge_value_with_timestamp(self):
        """Get value from motorcontroller for Bridge with timestamp."""
        data = self._node_brige_speed_feedback.read_data_value()
        return (data.Value.Value, data.SourceTimestamp.timestamp())


    def get_speed_hoist_value_with_timestamp(self):
        """Get value from motorcontroller for Bridge with timestamp."""
        data = self._node_hoist_speed_feedback.read_data_value()
        return (data.Value.Value, data.SourceTimestamp.timestamp())


    def get_speed_trolley_value_with_timestamp(self):
        """Get value from motorcontroller for Bridge with timestamp."""
        data = self._node_trolley_speed_feedback.read_data_value()
        return (data.Value.Value, data.SourceTimestamp.timestamp())


    """Crane target functions"""
    """Functions for setting targets for crane"""

    def set_target_bridge(self, target):
        """Set target value of bridge min the other crane, max 25146."""
        self.bridge_target = target


    def set_target_trolley(self, target):
        """Set target value of trolley min 285, max 8376."""
        self.trolley_target = target


    def set_target_hoist(self, target):
        """Set target value of Hoist."""
        self.hoist_target = target


    def set_moving_height(self, target):
        """Set target for moving height of Hoist."""
        self.hoist_moving_height = target


    def set_target_current_position(self):
        """Set current position to target"""
        x, y, z = self.get_coordinates_absolute()
        self.set_target_bridge(x)
        self.set_target_trolley(y)
        self.set_target_hoist(z)
        return x, y, z

    """Functions to get weight from the crane"""

    def get_load(self):
        """Get current load from crane."""
        return self._node_hoist_current_load.read_value()

    def get_load_tared(self):
        """Get current tared load from crane."""
        return self._node_hoist_current_tared_load.read_value()
    
    def get_datetime(self):
        """Get Python datetime object from the crane."""
        year = self._node_datime_year.read_value()
        month = self._node_datime_month.read_value()
        day = self._node_datime_day.read_value()
        hour = self._node_datime_hour.read_value()
        minute = self._node_datime_minute.read_value()
        second = self._node_datime_second.read_value()
        millisecond = self._node_datime_millisecond.read_value()
        return datetime.datetime(year,month,day,hour,minute,second,millisecond*1000)

    """Functions for getting distance to target"""

    def bridge_to_target(self):
        """Returns mm to pre-set target by set_target_bridge()."""
        return self.get_bridge_position_absolute() - self.bridge_target


    def trolley_to_target(self):
        """Returns mm to pre-set target by set_target_trolley()."""
        return self.get_trolley_position_absolute() - self.trolley_target


    def hoist_to_target(self):
        """Returns mm to pre-set target by set_target_hoist()."""
        return self.get_hoist_position_absolute() - self.hoist_target


    def hoist_to_moving_height(self):
        """Returns mm to pre-set target by set_moving_height()."""
        return self.get_hoist_position_absolute() - self.hoist_moving_height



    """Function to ramp cranes speed based on distance"""

    def ramp_speed(self, distance):
        """"Ramps the speed based on distance"""
        if -3 < distance < 3:
            speed = 0.3
        elif -5 < distance < 5:
            speed = 0.5
        elif -10 < distance < 10:
            speed = 1
        elif -50 < distance < 50:
            speed = 3
        elif -100 < distance < 100:
            speed = 8
        elif -300 < distance < 300:
            speed = 15
        else:
            speed = 20
        return speed


    def ramp_speed2(self, distance):
        """Ramps the speed based on distance, alternative option"""
        if -10 < distance < 10:
            speed = 2
        elif -300 < distance < 300:
            speed = abs(60.0*distance/300)
        else:
            speed = 30
        return speed


    def ramp_speed_horizontal(self, distance, fast=False):
        """Ramps the speed based on distance, optimized for horizontal movement.
            Use fast to limit minimum speed to certain value. Less accurate, but faster"""
        if -15 < distance < 15:
            speed = 0.6
        elif -2000 < distance < 2000:
            speed = abs(distance/20.0)
        else:
            speed = 100

        return 15 if fast and speed < 15 else speed


    def ramp_speed_lower(self, distance):
        """Ramps the speed based on distance, slow ramp for lowering"""
        if -8 < distance < 8:
            speed = 2
        elif -400 < distance < 400:
            speed = abs(distance/4.0)
        else:
            speed = 100
        return speed


    def ramp_speed_lift(self, distance):
        """Ramps the speed based on distance, fast ramp for lifting"""
        if -8 < distance < 8:
            speed = 4
        elif -200 < distance < 200:
            speed = abs(distance/2.0)
        else:
            speed = 100
        return speed



    """Premade functions for moving crane to target"""

    def move_trolley_to_target(self, threshold=1, fast=False):
        """Moves trolley to target"""

        # Retrieve updated distance to target
        dist_to_target = self.trolley_to_target()

        speed = self.ramp_speed_horizontal(dist_to_target, fast)

        if -threshold <= dist_to_target <= threshold:
            self.stop_trolley()
            print("Trolley on target")
            flag = 1
        elif dist_to_target > 0:
            self.move_trolley_backward_speed(speed)
            flag = 0
        else:
            self.move_trolley_forward_speed(speed)
            flag = 0

        return flag


    def move_bridge_to_target(self, threshold=1, fast=False):
        """Moves bridge to target"""

        # Retrieve updated distance to target
        dist_to_target = self.bridge_to_target()

        speed = self.ramp_speed_horizontal(dist_to_target, fast)

        if -threshold <= dist_to_target <= threshold:
            self.stop_bridge()
            print("Bridge on target")
            flag = 1
        elif dist_to_target > 0:
            self.move_bridge_backward_speed(speed)
            flag = 0
        else:
            self.move_bridge_forward_speed(speed)
            flag = 0

        return flag


    def move_hoist_to_target_precise(self, target):
        """
		Moves hoist to target by precision of 0.1 mm
		args:
			target: Hoist target position
		return:
			returns True if hoist is in target location
			False otherwise
		"""

        # Retrieve updated distance to target

        hoist_pos = self.get_motorcontroller_hoist_value()

        dist_to_target = target - hoist_pos

        speed = self.ramp_speed_lower(dist_to_target / 10)


        if dist_to_target < 0:
            self.move_hoist_down_speed(speed)
            return False
        if dist_to_target > 0:
            self.move_hoist_up_speed(speed)
            return False
        self.stop_hoist()
        return True


    def move_hoist_to_target(self, threshold=2, fast=False):
        """Moves hoist to target"""

        # Retrieve updated distance to target
        dist_to_target = self.hoist_to_target()

        hoist_pos = self.get_hoist_position_absolute()

        if fast:
            speed = self.ramp_speed_lift(dist_to_target)
        else:
            speed = self.ramp_speed_lower(dist_to_target)

        if -threshold <= dist_to_target <= threshold: 
            self.stop_hoist()
            print("Hoist in target")
            flag = 1
        elif dist_to_target > 0: 
            self.move_hoist_down_speed(speed)
            flag = 0
        else:
            self.move_hoist_up_speed(speed)
            flag = 0

        return flag
    

    def move_hoist_to_target_lift(self):
        """Moves hoist to target fast"""

        return self.move_hoist_to_target(fast=True)


    def move_hoist_to_moving_height(self):
        """Moves hoist to moving height fast"""

        # Retrieve updated distance to target
        dist_to_target = self.hoist_to_moving_height()

        hoist_pos = self.get_hoist_position_absolute()

        speed = self.ramp_speed_lift(dist_to_target)
        if hoist_pos > (self.hoist_moving_height):
            self.move_hoist_down_speed(speed)
            flag = 0
        elif hoist_pos < (self.hoist_moving_height):
            self.move_hoist_up_speed(speed)
            flag = 0
        else:
            self.stop_hoist()
            print("Hoist in moving height")
            flag = 1

        return flag



    """Premade functions for moving crane to target with P control"""

    def speedPcontrol(self, error):
        """Simple P control for speed"""
        max = 20 # saturation level = max output
        threshold = 150 # apply ramp below this error
        offset = 0 # minimum output

        Pgain = max/threshold

        speed = Pgain*abs(error)+offset

        return speed if speed <= max else max


    def move_trolley_to_target_p(self, precision=1):
        """Moves trolley to target"""

        # Retrieve updated distance to target
        dist_to_target = self.trolley_to_target()

        speed = self.speedPcontrol(dist_to_target)

        flag = 0
        if abs(dist_to_target) <= precision/2:
            self.stop_trolley()
            # print("Trolley on target")
            flag = 1
        elif dist_to_target > 0:
            self.move_trolley_backward_speed(speed)
        else:
            self.move_trolley_forward_speed(speed)

        return flag


    def move_bridge_to_target_p(self, precision=1):
        """Moves bridge to target"""

        # Retrieve updated distance to target
        dist_to_target = self.bridge_to_target()

        # speed = self.ramp_speed_horizontal(dist_to_target, fast)
        speed = self.speedPcontrol(dist_to_target)

        flag = 0
        if abs(dist_to_target) <= precision/2:
            self.stop_bridge()
            # print("Bridge on target")
            flag = 1
        elif dist_to_target > 0:
            self.move_bridge_backward_speed(speed)
        else:
            self.move_bridge_forward_speed(speed)

        return flag


    def move_hoist_to_target_p(self, precision=1):
        """Moves hoist to target"""

        # Retrieve updated distance to target
        dist_to_target = self.hoist_to_target()

        speed = self.speedPcontrol(dist_to_target)

        flag = 0
        if abs(dist_to_target) <= precision/2:
            self.stop_hoist()
            # print("Hoist in target")
            flag = 1
        elif dist_to_target > 0:
            self.move_hoist_down_speed(speed)
        else:
            self.move_hoist_up_speed(speed)

        return flag


    def move_hoist_to_moving_height_p(self):
        """Moves hoist to moving height fast"""

        stored_target = self.hoist_moving_height

        # Set current target to moving height
        self.hoist_target = self.hoist_moving_height

        flag = self.move_hoist_to_target()

        # Restore original target value
        self.hoist_target = stored_target

        return flag



    """Crane zeroing functions"""
    """Functions for zeroing cranes location"""

    def zero_hoist_position(self):
        """ Zero the motorcontroller value of Hoist"""
        self.hoist_last_zeroed = self.get_motorcontroller_hoist_value()


    def zero_trolley_position(self):
        """ Zero the motorcontroller value of Trolley"""
        self.trolley_last_zeroed = self.get_motorcontroller_trolley_value()


    def zero_bridge_position(self):
        """ Zero the motorcontroller value of Bridge"""
        self.bridge_last_zeroed = self.get_motorcontroller_bridge_value()



    """Functions for getting cranes zeroed location"""

    def get_zero_bridge_position(self):
        """Get last zeroed value of Bridge"""
        return self.bridge_last_zeroed


    def get_zero_trolley_position(self):
        """Get last zeroed value of Trolley"""
        return self.trolley_last_zeroed


    def get_zero_hoist_position(self):
        """Get last zeroed value of Hoist"""
        return self.hoist_last_zeroed



    """Functions for getting distance to cranes zeroed location"""

    def get_difference_hoist_to_zero(self):
        """Difference from Hoist to last zeroed value."""
        return self.get_motorcontroller_hoist_value() - self.get_zero_hoist_position()


    def get_difference_trolley_to_zero(self):
        """Difference from Trolley to last zeroed value."""
        return self.get_motorcontroller_trolley_value() - self.get_zero_trolley_position()


    def get_difference_bridge_to_zero(self):
        """Difference from Bridge to last zeroed value."""
        return self.get_motorcontroller_bridge_value() - self.get_zero_bridge_position()


    def get_difference_all_to_zero(self):
        """Difference from all axis to the last zeroed values, B,T,H."""
        return(self.get_difference_bridge_to_zero(),
               self.get_difference_trolley_to_zero(),
               self.get_difference_hoist_to_zero())



    """Functions for setting cranes movement directions"""

    def move_trolley_forward(self, boolean=True):
        """Set Move Trolley Forwardtrue or false."""
        self._node_trolley_forward.write_value(ua.DataValue(ua.Variant(
            boolean, ua.VariantType.Boolean)))


    def move_trolley_backward(self, boolean=True):
        """Set Move Trolley Backward true or false."""
        self._node_trolley_backward.write_value(ua.DataValue(ua.Variant(
            boolean, ua.VariantType.Boolean)))


    def move_bridge_forward(self, boolean=True):
        """Set Move Bridge Forward true or false."""
        self._node_bridge_forward.write_value(ua.DataValue(ua.Variant(
            boolean, ua.VariantType.Boolean)))

    def move_bridge_backward(self, boolean=True):
        """Set Move Bridge Backward  true or false."""
        self._node_bridge_backward.write_value(ua.DataValue(ua.Variant(
            boolean, ua.VariantType.Boolean)))


    def move_hoist_up(self, boolean=True):
        """Set Move Hoist up true or false."""
        self._node_hoist_up.write_value(ua.DataValue(ua.Variant(
            boolean, ua.VariantType.Boolean)))


    def move_hoist_down(self, boolean=True):
        """Set Move Hoist down true or false."""
        self._node_hoist_down.write_value(ua.DataValue(ua.Variant(
            boolean, ua.VariantType.Boolean)))



    """Functions for getting boolean values of cranes movement directions"""

    def get_trolley_forward(self):
        """Get Trolley_Forward boolean value."""
        return self._node_trolley_forward.read_value()


    def get_trolley_backward(self):
        """Get Trolley_Backward boolean value."""
        return self._node_trolley_backward.read_value()


    def get_bridge_forward(self):
        """Get Bridge_Forward boolean value."""
        return self._node_bridge_forward.read_value()


    def get_bridge_backward(self):
        """Get Bridge_Backward boolean value."""
        return self._node_bridge_backward.read_value()


    def get_hoist_up(self):
        """Get Hoist_up boolean value."""
        return self._node_hoist_up.read_value()


    def get_hoist_down(self):
        """Get Hoist_down boolean value."""
        return self._node_hoist_down.read_value()



    """Functions to set cranes speed"""

    def set_trolley_speed(self, speed):
        """Set speed Trolley in % 0-100"""
        self._node_trolley_speed.write_value(ua.DataValue(ua.Variant(
            speed, ua.VariantType.Float)))


    def set_bridge_speed(self, speed):
        """Set speed Bridge in % 0-100"""
        self._node_bridge_speed.write_value(ua.DataValue(ua.Variant(
            speed, ua.VariantType.Float)))


    def set_hoist_speed(self, speed):
        """Set speed Hoist in % 0-100"""
        self._node_hoist_speed.write_value(ua.DataValue(ua.Variant(
            speed, ua.VariantType.Float)))



    """Functions to get cranes speed"""

    def get_trolley_speed(self):
        """Get speed Trolley in % 0-100"""
        return self._node_trolley_speed.read_value()


    def get_bridge_speed(self):
        """Get speed Bridge in % 0-100"""
        return self._node_bridge_speed.read_value()


    def get_hoist_speed(self):
        """Get speed Hoist in % 0-100"""
        return self._node_hoist_speed.read_value()



    """Functions to set crane move with specific speed to specific deirection"""

    def move_trolley_forward_speed(self, speed):
        """Move trolley direction forward with speed"""
        self.move_trolley_backward(False)
        self.move_trolley_forward(True)
        self.set_trolley_speed(speed)
        return True


    def move_trolley_backward_speed(self, speed):
        """Move trolley direction backward with speed"""
        self.move_trolley_forward(False)
        self.move_trolley_backward(True)
        self.set_trolley_speed(speed)
        return True


    def move_bridge_forward_speed(self, speed):
        """Move bridge direction forward with speed"""
        self.move_bridge_backward(False)
        self.move_bridge_forward(True)
        self.set_bridge_speed(speed)
        return True


    def move_bridge_backward_speed(self, speed):
        """Move bridge direction backward with speed"""
        self.move_bridge_forward(False)
        self.move_bridge_backward(True)
        self.set_bridge_speed(speed)
        return True


    def move_hoist_down_speed(self, speed):
        """Move hoist direction forward with speed"""
        self.move_hoist_up(False)
        self.move_hoist_down(True)
        self.set_hoist_speed(speed)
        return True


    def move_hoist_up_speed(self, speed):
        """Move hoist direction backward with speed"""
        self.move_hoist_down(False)
        self.move_hoist_up(True)
        self.set_hoist_speed(speed)
        return True



    """Functions for stopping crane"""

    def stop_bridge(self):
        """Stop Bridge"""
        self.set_bridge_speed(0)
        self.move_bridge_forward(False)
        self.move_bridge_backward(False)


    def stop_trolley(self):
        """Stop Trolley"""
        self.set_trolley_speed(0)
        self.move_trolley_forward(False)
        self.move_trolley_backward(False)


    def stop_hoist(self):
        """Stop Hoist"""
        self.set_hoist_speed(0)
        self.move_hoist_up(False)
        self.move_hoist_down(False)


    def stop_all(self):
        """Stop all 3 axis"""
        self.stop_bridge()
        self.stop_trolley()
        self.stop_hoist()



    """Crane control signal status"""

    def get_trolley_speed_request(self):
        """ Get requested/target speed (ref), return negative if request is backward """
        inv = -1 if self._node_trolley_direction_backwards_request.read_value() else 1
        return inv*self._node_trolley_speed_request.read_value()


    def get_trolley_speed_feedback(self):
        return self._node_trolley_speed_feedback.read_value()


    def get_trolley_speed_feedback_mmin(self):
        return self._node_trolley_speed_feedback_mmin.read_value()


    def get_trolley_status(self):
        """ Gets the position, target speed and actual speed. Speed request is negative if request is backward """
        return self.get_trolley_position_absolute(), self.get_trolley_speed_request(), self.get_trolley_speed_feedback(), self.get_trolley_speed_feedback_mmin()


    def get_bridge_speed_request(self):
        """ Get requested/target speed (ref), return negative if request is backward """
        inv = -1 if self._node_bridge_direction_backward_request.read_value() else 1
        return inv*self._node_bridge_speed_request.read_value()


    def get_bridge_speed_feedback(self):
        return self._node_brige_speed_feedback.read_value()


    def get_bridge_speed_feedback_mmin(self):
        return self._node_brige_speed_feedback_mmin.read_value()


    def get_bridge_status(self):
        """ Gets the position, target speed and actual speed. Speed is negative if request is backward """
        return self.get_bridge_position_absolute(), self.get_bridge_speed_request(), self.get_bridge_speed_feedback(), self.get_bridge_speed_feedback_mmin()


    def get_hoist_speed_feedback(self):
        return self._node_hoist_speed_feedback.read_value()


    def get_hoist_speed_feedback_mmin(self):
        return self._node_hoist_speed_feedback_mmin.read_value()


    def get_hoist_speed_request(self):
        """ Get requested/target speed (ref), return negative if request is down """
        inv = -1 if self._node_hoist_direction_down_request.read_value() else 1
        return inv*self._node_hoist_speed_request.read_value()


    def get_hoist_status(self):
        """ Gets the position, target speed and actual speed. Speed is negative if request is down """
        return self.get_hoist_position_absolute(), self.get_hoist_speed_request(), self.get_hoist_speed_feedback(), self.get_hoist_speed_feedback_mmin()


    """Functions for subscribing to cranes data"""

    class SubHandler:
        """Used with subscriptions"""

        def __init__(self, queue):
            self.queue = queue

        def datachange_notification(self, node, value, data):
            """Puts data in queue from subscripted node"""
            self.queue.put(
                [data.monitored_item.Value.Value.Value,
                 data.monitored_item.Value.SourceTimestamp.timestamp()])


    def sub_trolley(self, interval, queue):
        """
        subscribes to trolleys position.
        Interval is how often data is updated from wanted node in ms.
        Queue is the queue where data will be put
        """

        handler = self.SubHandler(queue)
        sub = self.client.create_subscription(interval, handler)
        var = self._node_trolley_position_mm
        handle = sub.subscribe_data_change(var)

        # subscription can be ended by writing:
        # sub.unsubscribe(handle)
        return sub, handle


    def sub_bridge(self, interval, queue):
        """
        subscribes to bridges position.
        Interval is how often data is updated from wanted node in ms.
        Queue is the queue where data will be put
        """

        handler = self.SubHandler(queue)
        sub = self.client.create_subscription(interval, handler)
        var = self._node_bridge_position_mm
        handle = sub.subscribe_data_change(var)

        # subscription can be ended by writing:
        # sub.unsubscribe(handle)
        return sub, handle


    def sub_hoist(self, interval, queue):
        """
        subscribes to trolleys position.
        Interval is how often data is updated from wanted node in ms.
        Queue is the queue where data will be put
        """

        handler = self.SubHandler(queue)
        sub = self.client.create_subscription(interval, handler)
        var = self._node_hoist_position_mm
        handle = sub.subscribe_data_change(var)

        # subscription can be ended by writing:
        # sub.unsubscribe(handle)
        return sub, handle


    def sub_trolley_speed(self, interval, queue):
        """
        subscribes to trolleys speed.
        Interval is how often data is updated from wanted node in ms.
        Queue is the queue where data will be put
        """

        handler = self.SubHandler(queue)
        sub = self.client.create_subscription(interval, handler)
        var = self._node_trolley_speed_feedback
        handle = sub.subscribe_data_change(var)

        return sub, handle


    def sub_bridge_speed(self, interval, queue):
        """
        subscribes to bridges speed.
        Interval is how often data is updated from wanted node in ms.
        Queue is the queue where data will be put
        """

        handler = self.SubHandler(queue)
        sub = self.client.create_subscription(interval, handler)
        var = self._node_brige_speed_feedback
        handle = sub.subscribe_data_change(var)

        return sub, handle

    def sub_hoist_speed(self, interval, queue):
        """
        subscribes to hoists speed.
        Interval is how often data is updated from wanted node in ms.
        Queue is the queue where data will be put
        """

        handler = self.SubHandler(queue)
        sub = self.client.create_subscription(interval, handler)
        var = self._node_hoist_speed_feedback
        handle = sub.subscribe_data_change(var)

        return sub, handle

