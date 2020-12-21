# This Python file uses the following encoding: utf-8
"""autogenerated by genpy from visp_ros/PoseStampedStatus.msg. Do not edit."""
import sys
python3 = True if sys.hexversion > 0x03000000 else False
import genpy
import struct

import geometry_msgs.msg
import std_msgs.msg

class PoseStampedStatus(genpy.Message):
  _md5sum = "71ae8a9e7c5c6a036498a62872a0dbc4"
  _type = "visp_ros/PoseStampedStatus"
  _has_header = False #flag to mark the presence of a Header object
  _full_text = """int8 status
geometry_msgs/PoseStamped pose_stamped

================================================================================
MSG: geometry_msgs/PoseStamped
# A Pose with reference coordinate frame and timestamp
Header header
Pose pose

================================================================================
MSG: std_msgs/Header
# Standard metadata for higher-level stamped data types.
# This is generally used to communicate timestamped data 
# in a particular coordinate frame.
# 
# sequence ID: consecutively increasing ID 
uint32 seq
#Two-integer timestamp that is expressed as:
# * stamp.sec: seconds (stamp_secs) since epoch (in Python the variable is called 'secs')
# * stamp.nsec: nanoseconds since stamp_secs (in Python the variable is called 'nsecs')
# time-handling sugar is provided by the client library
time stamp
#Frame this data is associated with
# 0: no frame
# 1: global frame
string frame_id

================================================================================
MSG: geometry_msgs/Pose
# A representation of pose in free space, composed of position and orientation. 
Point position
Quaternion orientation

================================================================================
MSG: geometry_msgs/Point
# This contains the position of a point in free space
float64 x
float64 y
float64 z

================================================================================
MSG: geometry_msgs/Quaternion
# This represents an orientation in free space in quaternion form.

float64 x
float64 y
float64 z
float64 w
"""
  __slots__ = ['status','pose_stamped']
  _slot_types = ['int8','geometry_msgs/PoseStamped']

  def __init__(self, *args, **kwds):
    """
    Constructor. Any message fields that are implicitly/explicitly
    set to None will be assigned a default value. The recommend
    use is keyword arguments as this is more robust to future message
    changes.  You cannot mix in-order arguments and keyword arguments.

    The available fields are:
       status,pose_stamped

    :param args: complete set of field values, in .msg order
    :param kwds: use keyword arguments corresponding to message field names
    to set specific fields.
    """
    if args or kwds:
      super(PoseStampedStatus, self).__init__(*args, **kwds)
      #message fields cannot be None, assign default values for those that are
      if self.status is None:
        self.status = 0
      if self.pose_stamped is None:
        self.pose_stamped = geometry_msgs.msg.PoseStamped()
    else:
      self.status = 0
      self.pose_stamped = geometry_msgs.msg.PoseStamped()

  def _get_types(self):
    """
    internal API method
    """
    return self._slot_types

  def serialize(self, buff):
    """
    serialize message into buffer
    :param buff: buffer, ``StringIO``
    """
    try:
      _x = self
      buff.write(_get_struct_b3I().pack(_x.status, _x.pose_stamped.header.seq, _x.pose_stamped.header.stamp.secs, _x.pose_stamped.header.stamp.nsecs))
      _x = self.pose_stamped.header.frame_id
      length = len(_x)
      if python3 or type(_x) == unicode:
        _x = _x.encode('utf-8')
        length = len(_x)
      buff.write(struct.pack('<I%ss'%length, length, _x))
      _x = self
      buff.write(_get_struct_7d().pack(_x.pose_stamped.pose.position.x, _x.pose_stamped.pose.position.y, _x.pose_stamped.pose.position.z, _x.pose_stamped.pose.orientation.x, _x.pose_stamped.pose.orientation.y, _x.pose_stamped.pose.orientation.z, _x.pose_stamped.pose.orientation.w))
    except struct.error as se: self._check_types(struct.error("%s: '%s' when writing '%s'" % (type(se), str(se), str(locals().get('_x', self)))))
    except TypeError as te: self._check_types(ValueError("%s: '%s' when writing '%s'" % (type(te), str(te), str(locals().get('_x', self)))))

  def deserialize(self, str):
    """
    unpack serialized message in str into this message instance
    :param str: byte array of serialized message, ``str``
    """
    try:
      if self.pose_stamped is None:
        self.pose_stamped = geometry_msgs.msg.PoseStamped()
      end = 0
      _x = self
      start = end
      end += 13
      (_x.status, _x.pose_stamped.header.seq, _x.pose_stamped.header.stamp.secs, _x.pose_stamped.header.stamp.nsecs,) = _get_struct_b3I().unpack(str[start:end])
      start = end
      end += 4
      (length,) = _struct_I.unpack(str[start:end])
      start = end
      end += length
      if python3:
        self.pose_stamped.header.frame_id = str[start:end].decode('utf-8')
      else:
        self.pose_stamped.header.frame_id = str[start:end]
      _x = self
      start = end
      end += 56
      (_x.pose_stamped.pose.position.x, _x.pose_stamped.pose.position.y, _x.pose_stamped.pose.position.z, _x.pose_stamped.pose.orientation.x, _x.pose_stamped.pose.orientation.y, _x.pose_stamped.pose.orientation.z, _x.pose_stamped.pose.orientation.w,) = _get_struct_7d().unpack(str[start:end])
      return self
    except struct.error as e:
      raise genpy.DeserializationError(e) #most likely buffer underfill


  def serialize_numpy(self, buff, numpy):
    """
    serialize message with numpy array types into buffer
    :param buff: buffer, ``StringIO``
    :param numpy: numpy python module
    """
    try:
      _x = self
      buff.write(_get_struct_b3I().pack(_x.status, _x.pose_stamped.header.seq, _x.pose_stamped.header.stamp.secs, _x.pose_stamped.header.stamp.nsecs))
      _x = self.pose_stamped.header.frame_id
      length = len(_x)
      if python3 or type(_x) == unicode:
        _x = _x.encode('utf-8')
        length = len(_x)
      buff.write(struct.pack('<I%ss'%length, length, _x))
      _x = self
      buff.write(_get_struct_7d().pack(_x.pose_stamped.pose.position.x, _x.pose_stamped.pose.position.y, _x.pose_stamped.pose.position.z, _x.pose_stamped.pose.orientation.x, _x.pose_stamped.pose.orientation.y, _x.pose_stamped.pose.orientation.z, _x.pose_stamped.pose.orientation.w))
    except struct.error as se: self._check_types(struct.error("%s: '%s' when writing '%s'" % (type(se), str(se), str(locals().get('_x', self)))))
    except TypeError as te: self._check_types(ValueError("%s: '%s' when writing '%s'" % (type(te), str(te), str(locals().get('_x', self)))))

  def deserialize_numpy(self, str, numpy):
    """
    unpack serialized message in str into this message instance using numpy for array types
    :param str: byte array of serialized message, ``str``
    :param numpy: numpy python module
    """
    try:
      if self.pose_stamped is None:
        self.pose_stamped = geometry_msgs.msg.PoseStamped()
      end = 0
      _x = self
      start = end
      end += 13
      (_x.status, _x.pose_stamped.header.seq, _x.pose_stamped.header.stamp.secs, _x.pose_stamped.header.stamp.nsecs,) = _get_struct_b3I().unpack(str[start:end])
      start = end
      end += 4
      (length,) = _struct_I.unpack(str[start:end])
      start = end
      end += length
      if python3:
        self.pose_stamped.header.frame_id = str[start:end].decode('utf-8')
      else:
        self.pose_stamped.header.frame_id = str[start:end]
      _x = self
      start = end
      end += 56
      (_x.pose_stamped.pose.position.x, _x.pose_stamped.pose.position.y, _x.pose_stamped.pose.position.z, _x.pose_stamped.pose.orientation.x, _x.pose_stamped.pose.orientation.y, _x.pose_stamped.pose.orientation.z, _x.pose_stamped.pose.orientation.w,) = _get_struct_7d().unpack(str[start:end])
      return self
    except struct.error as e:
      raise genpy.DeserializationError(e) #most likely buffer underfill

_struct_I = genpy.struct_I
def _get_struct_I():
    global _struct_I
    return _struct_I
_struct_7d = None
def _get_struct_7d():
    global _struct_7d
    if _struct_7d is None:
        _struct_7d = struct.Struct("<7d")
    return _struct_7d
_struct_b3I = None
def _get_struct_b3I():
    global _struct_b3I
    if _struct_b3I is None:
        _struct_b3I = struct.Struct("<b3I")
    return _struct_b3I