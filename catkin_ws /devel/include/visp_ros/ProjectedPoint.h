// Generated by gencpp from file visp_ros/ProjectedPoint.msg
// DO NOT EDIT!


#ifndef VISP_ROS_MESSAGE_PROJECTEDPOINT_H
#define VISP_ROS_MESSAGE_PROJECTEDPOINT_H


#include <string>
#include <vector>
#include <map>

#include <ros/types.h>
#include <ros/serialization.h>
#include <ros/builtin_message_traits.h>
#include <ros/message_operations.h>


namespace visp_ros
{
template <class ContainerAllocator>
struct ProjectedPoint_
{
  typedef ProjectedPoint_<ContainerAllocator> Type;

  ProjectedPoint_()
    : x(0.0)
    , y(0.0)  {
    }
  ProjectedPoint_(const ContainerAllocator& _alloc)
    : x(0.0)
    , y(0.0)  {
  (void)_alloc;
    }



   typedef double _x_type;
  _x_type x;

   typedef double _y_type;
  _y_type y;





  typedef boost::shared_ptr< ::visp_ros::ProjectedPoint_<ContainerAllocator> > Ptr;
  typedef boost::shared_ptr< ::visp_ros::ProjectedPoint_<ContainerAllocator> const> ConstPtr;

}; // struct ProjectedPoint_

typedef ::visp_ros::ProjectedPoint_<std::allocator<void> > ProjectedPoint;

typedef boost::shared_ptr< ::visp_ros::ProjectedPoint > ProjectedPointPtr;
typedef boost::shared_ptr< ::visp_ros::ProjectedPoint const> ProjectedPointConstPtr;

// constants requiring out of line definition



template<typename ContainerAllocator>
std::ostream& operator<<(std::ostream& s, const ::visp_ros::ProjectedPoint_<ContainerAllocator> & v)
{
ros::message_operations::Printer< ::visp_ros::ProjectedPoint_<ContainerAllocator> >::stream(s, "", v);
return s;
}

} // namespace visp_ros

namespace ros
{
namespace message_traits
{



// BOOLTRAITS {'IsFixedSize': True, 'IsMessage': True, 'HasHeader': False}
// {'sensor_msgs': ['/opt/ros/kinetic/share/sensor_msgs/cmake/../msg'], 'visp_ros': ['/home/user/catkin_ws/src/visp_ros/msg'], 'std_msgs': ['/opt/ros/kinetic/share/std_msgs/cmake/../msg'], 'geometry_msgs': ['/opt/ros/kinetic/share/geometry_msgs/cmake/../msg']}

// !!!!!!!!!!! ['__class__', '__delattr__', '__dict__', '__doc__', '__eq__', '__format__', '__getattribute__', '__hash__', '__init__', '__module__', '__ne__', '__new__', '__reduce__', '__reduce_ex__', '__repr__', '__setattr__', '__sizeof__', '__str__', '__subclasshook__', '__weakref__', '_parsed_fields', 'constants', 'fields', 'full_name', 'has_header', 'header_present', 'names', 'package', 'parsed_fields', 'short_name', 'text', 'types']




template <class ContainerAllocator>
struct IsFixedSize< ::visp_ros::ProjectedPoint_<ContainerAllocator> >
  : TrueType
  { };

template <class ContainerAllocator>
struct IsFixedSize< ::visp_ros::ProjectedPoint_<ContainerAllocator> const>
  : TrueType
  { };

template <class ContainerAllocator>
struct IsMessage< ::visp_ros::ProjectedPoint_<ContainerAllocator> >
  : TrueType
  { };

template <class ContainerAllocator>
struct IsMessage< ::visp_ros::ProjectedPoint_<ContainerAllocator> const>
  : TrueType
  { };

template <class ContainerAllocator>
struct HasHeader< ::visp_ros::ProjectedPoint_<ContainerAllocator> >
  : FalseType
  { };

template <class ContainerAllocator>
struct HasHeader< ::visp_ros::ProjectedPoint_<ContainerAllocator> const>
  : FalseType
  { };


template<class ContainerAllocator>
struct MD5Sum< ::visp_ros::ProjectedPoint_<ContainerAllocator> >
{
  static const char* value()
  {
    return "209f516d3eb691f0663e25cb750d67c1";
  }

  static const char* value(const ::visp_ros::ProjectedPoint_<ContainerAllocator>&) { return value(); }
  static const uint64_t static_value1 = 0x209f516d3eb691f0ULL;
  static const uint64_t static_value2 = 0x663e25cb750d67c1ULL;
};

template<class ContainerAllocator>
struct DataType< ::visp_ros::ProjectedPoint_<ContainerAllocator> >
{
  static const char* value()
  {
    return "visp_ros/ProjectedPoint";
  }

  static const char* value(const ::visp_ros::ProjectedPoint_<ContainerAllocator>&) { return value(); }
};

template<class ContainerAllocator>
struct Definition< ::visp_ros::ProjectedPoint_<ContainerAllocator> >
{
  static const char* value()
  {
    return "# Message corresponding to coordinates of the point after perspective projection\n\
float64 x      # Coordinate of the point in the image plane in meter along X axis\n\
float64 y      # Coordinate of the point in the image plane in meter along Y axis\n\
\n\
";
  }

  static const char* value(const ::visp_ros::ProjectedPoint_<ContainerAllocator>&) { return value(); }
};

} // namespace message_traits
} // namespace ros

namespace ros
{
namespace serialization
{

  template<class ContainerAllocator> struct Serializer< ::visp_ros::ProjectedPoint_<ContainerAllocator> >
  {
    template<typename Stream, typename T> inline static void allInOne(Stream& stream, T m)
    {
      stream.next(m.x);
      stream.next(m.y);
    }

    ROS_DECLARE_ALLINONE_SERIALIZER
  }; // struct ProjectedPoint_

} // namespace serialization
} // namespace ros

namespace ros
{
namespace message_operations
{

template<class ContainerAllocator>
struct Printer< ::visp_ros::ProjectedPoint_<ContainerAllocator> >
{
  template<typename Stream> static void stream(Stream& s, const std::string& indent, const ::visp_ros::ProjectedPoint_<ContainerAllocator>& v)
  {
    s << indent << "x: ";
    Printer<double>::stream(s, indent + "  ", v.x);
    s << indent << "y: ";
    Printer<double>::stream(s, indent + "  ", v.y);
  }
};

} // namespace message_operations
} // namespace ros

#endif // VISP_ROS_MESSAGE_PROJECTEDPOINT_H
