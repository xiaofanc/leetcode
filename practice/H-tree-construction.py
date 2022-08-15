
# drawline(x1, y1, x2, y2)

def drawHTree(x, y, length, depth):
  # get the coordinates of the endpoints of H
  if depth == 0:
    return
  leftbottom = [x-length/2, y-length/2]
  lefttop = [x-length/2, y+length/2]
  rightbottom = [x+length/2, y-length/2]
  righttop = [x+length/2, y+length/2]
  
  drawline([x-length/2, y], [x+length/2, y])
  drawline(leftbottom, lefttop)
  drawline(rightbottom, righttop)
  
  # Time: O(4^depth), Space: O(depth)
  drawHTree(leftbottom[0], leftbottom[1], length/math.sqrt(2), depth-1)
  drawHTree(lefttop[0], lefttop[1], length/math.sqrt(2), depth-1)
  drawHTree(rightbottom[0], rightbottom[1], length/math.sqrt(2), depth-1)
  drawHTree(righttop[0], righttop[1], length/math.sqrt(2), depth-1)
  