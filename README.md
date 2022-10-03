# clipboard_modifier
 
When this script is running, any css taken with "copy CSS" action in Photoshop will be changed in clipboard, to include only position and size info (left, top, width, height).
This transforms the string in clipboard, such as this:
```
.Group_34 {
  background-image: url("Group 34.png");
  position: absolute;
  left: 138px;
  top: 110px;
  width: 149px;
  height: 79px;
  z-index: 7;
}
```
into this:
```
left: 138px;
top: 110px;
width: 149px;
height: 79px;
```
