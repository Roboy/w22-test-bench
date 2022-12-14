# This Python file uses the following encoding: utf-8
"""autogenerated by genpy from bench/BenchState.msg. Do not edit."""
import codecs
import sys
python3 = True if sys.hexversion > 0x03000000 else False
import genpy
import struct


class BenchState(genpy.Message):
  _md5sum = "5e6318cc4849f33a839d0d132a6048f8"
  _type = "bench/BenchState"
  _has_header = False  # flag to mark the presence of a Header object
  _full_text = """float32 angle

bool safety_switch_pressed

float32 flex_myobrick_pos_encoder
float32 flex_myobrick_torque_encoder
float32 flex_myobrick_current
float32 flex_myobrick_pwm
bool flex_myobrick_in_running_state

float32 extend_myobrick_pos_encoder
float32 extend_myobrick_torque_encoder
float32 extend_myobrick_current
float32 extend_myobrick_pwm
bool extend_myobrick_in_running_state

"""
  __slots__ = ['angle','safety_switch_pressed','flex_myobrick_pos_encoder','flex_myobrick_torque_encoder','flex_myobrick_current','flex_myobrick_pwm','flex_myobrick_in_running_state','extend_myobrick_pos_encoder','extend_myobrick_torque_encoder','extend_myobrick_current','extend_myobrick_pwm','extend_myobrick_in_running_state']
  _slot_types = ['float32','bool','float32','float32','float32','float32','bool','float32','float32','float32','float32','bool']

  def __init__(self, *args, **kwds):
    """
    Constructor. Any message fields that are implicitly/explicitly
    set to None will be assigned a default value. The recommend
    use is keyword arguments as this is more robust to future message
    changes.  You cannot mix in-order arguments and keyword arguments.

    The available fields are:
       angle,safety_switch_pressed,flex_myobrick_pos_encoder,flex_myobrick_torque_encoder,flex_myobrick_current,flex_myobrick_pwm,flex_myobrick_in_running_state,extend_myobrick_pos_encoder,extend_myobrick_torque_encoder,extend_myobrick_current,extend_myobrick_pwm,extend_myobrick_in_running_state

    :param args: complete set of field values, in .msg order
    :param kwds: use keyword arguments corresponding to message field names
    to set specific fields.
    """
    if args or kwds:
      super(BenchState, self).__init__(*args, **kwds)
      # message fields cannot be None, assign default values for those that are
      if self.angle is None:
        self.angle = 0.
      if self.safety_switch_pressed is None:
        self.safety_switch_pressed = False
      if self.flex_myobrick_pos_encoder is None:
        self.flex_myobrick_pos_encoder = 0.
      if self.flex_myobrick_torque_encoder is None:
        self.flex_myobrick_torque_encoder = 0.
      if self.flex_myobrick_current is None:
        self.flex_myobrick_current = 0.
      if self.flex_myobrick_pwm is None:
        self.flex_myobrick_pwm = 0.
      if self.flex_myobrick_in_running_state is None:
        self.flex_myobrick_in_running_state = False
      if self.extend_myobrick_pos_encoder is None:
        self.extend_myobrick_pos_encoder = 0.
      if self.extend_myobrick_torque_encoder is None:
        self.extend_myobrick_torque_encoder = 0.
      if self.extend_myobrick_current is None:
        self.extend_myobrick_current = 0.
      if self.extend_myobrick_pwm is None:
        self.extend_myobrick_pwm = 0.
      if self.extend_myobrick_in_running_state is None:
        self.extend_myobrick_in_running_state = False
    else:
      self.angle = 0.
      self.safety_switch_pressed = False
      self.flex_myobrick_pos_encoder = 0.
      self.flex_myobrick_torque_encoder = 0.
      self.flex_myobrick_current = 0.
      self.flex_myobrick_pwm = 0.
      self.flex_myobrick_in_running_state = False
      self.extend_myobrick_pos_encoder = 0.
      self.extend_myobrick_torque_encoder = 0.
      self.extend_myobrick_current = 0.
      self.extend_myobrick_pwm = 0.
      self.extend_myobrick_in_running_state = False

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
      buff.write(_get_struct_fB4fB4fB().pack(_x.angle, _x.safety_switch_pressed, _x.flex_myobrick_pos_encoder, _x.flex_myobrick_torque_encoder, _x.flex_myobrick_current, _x.flex_myobrick_pwm, _x.flex_myobrick_in_running_state, _x.extend_myobrick_pos_encoder, _x.extend_myobrick_torque_encoder, _x.extend_myobrick_current, _x.extend_myobrick_pwm, _x.extend_myobrick_in_running_state))
    except struct.error as se: self._check_types(struct.error("%s: '%s' when writing '%s'" % (type(se), str(se), str(locals().get('_x', self)))))
    except TypeError as te: self._check_types(ValueError("%s: '%s' when writing '%s'" % (type(te), str(te), str(locals().get('_x', self)))))

  def deserialize(self, str):
    """
    unpack serialized message in str into this message instance
    :param str: byte array of serialized message, ``str``
    """
    if python3:
      codecs.lookup_error("rosmsg").msg_type = self._type
    try:
      end = 0
      _x = self
      start = end
      end += 39
      (_x.angle, _x.safety_switch_pressed, _x.flex_myobrick_pos_encoder, _x.flex_myobrick_torque_encoder, _x.flex_myobrick_current, _x.flex_myobrick_pwm, _x.flex_myobrick_in_running_state, _x.extend_myobrick_pos_encoder, _x.extend_myobrick_torque_encoder, _x.extend_myobrick_current, _x.extend_myobrick_pwm, _x.extend_myobrick_in_running_state,) = _get_struct_fB4fB4fB().unpack(str[start:end])
      self.safety_switch_pressed = bool(self.safety_switch_pressed)
      self.flex_myobrick_in_running_state = bool(self.flex_myobrick_in_running_state)
      self.extend_myobrick_in_running_state = bool(self.extend_myobrick_in_running_state)
      return self
    except struct.error as e:
      raise genpy.DeserializationError(e)  # most likely buffer underfill


  def serialize_numpy(self, buff, numpy):
    """
    serialize message with numpy array types into buffer
    :param buff: buffer, ``StringIO``
    :param numpy: numpy python module
    """
    try:
      _x = self
      buff.write(_get_struct_fB4fB4fB().pack(_x.angle, _x.safety_switch_pressed, _x.flex_myobrick_pos_encoder, _x.flex_myobrick_torque_encoder, _x.flex_myobrick_current, _x.flex_myobrick_pwm, _x.flex_myobrick_in_running_state, _x.extend_myobrick_pos_encoder, _x.extend_myobrick_torque_encoder, _x.extend_myobrick_current, _x.extend_myobrick_pwm, _x.extend_myobrick_in_running_state))
    except struct.error as se: self._check_types(struct.error("%s: '%s' when writing '%s'" % (type(se), str(se), str(locals().get('_x', self)))))
    except TypeError as te: self._check_types(ValueError("%s: '%s' when writing '%s'" % (type(te), str(te), str(locals().get('_x', self)))))

  def deserialize_numpy(self, str, numpy):
    """
    unpack serialized message in str into this message instance using numpy for array types
    :param str: byte array of serialized message, ``str``
    :param numpy: numpy python module
    """
    if python3:
      codecs.lookup_error("rosmsg").msg_type = self._type
    try:
      end = 0
      _x = self
      start = end
      end += 39
      (_x.angle, _x.safety_switch_pressed, _x.flex_myobrick_pos_encoder, _x.flex_myobrick_torque_encoder, _x.flex_myobrick_current, _x.flex_myobrick_pwm, _x.flex_myobrick_in_running_state, _x.extend_myobrick_pos_encoder, _x.extend_myobrick_torque_encoder, _x.extend_myobrick_current, _x.extend_myobrick_pwm, _x.extend_myobrick_in_running_state,) = _get_struct_fB4fB4fB().unpack(str[start:end])
      self.safety_switch_pressed = bool(self.safety_switch_pressed)
      self.flex_myobrick_in_running_state = bool(self.flex_myobrick_in_running_state)
      self.extend_myobrick_in_running_state = bool(self.extend_myobrick_in_running_state)
      return self
    except struct.error as e:
      raise genpy.DeserializationError(e)  # most likely buffer underfill

_struct_I = genpy.struct_I
def _get_struct_I():
    global _struct_I
    return _struct_I
_struct_fB4fB4fB = None
def _get_struct_fB4fB4fB():
    global _struct_fB4fB4fB
    if _struct_fB4fB4fB is None:
        _struct_fB4fB4fB = struct.Struct("<fB4fB4fB")
    return _struct_fB4fB4fB
