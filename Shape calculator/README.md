## Sea level predictor

Dev. by : **Radwane Ait Ouhani**.

Context : **'Scientific Computing with python'**  certification project on **FreeCodeCamp**. 

### The idea :

Calculate the area, perimeter, diagonal and draw a picture of any given square or rectangle.    
Using object oriented programming to create a `Rectangle` class and a `Square` class. 
The `Square` class should be a subclass of `Rectangle` and inherit methods and attributes.

The `Rectangle` class contain the following methods:

* `set_width`
* `set_height`
* `get_area`: Returns area (`width`*`height`)
* `get_perimeter`: Returns perimeter (2 * `width` + 2 * `height`)
* `get_diagonal`: Returns diagonal ((width ** 2 + height ** 2) ** .5)
* `get_picture`: Returns a string that represents the shape using lines of "*".  If the 
width or height is larger than 50, this should return the string: "Too big for 
picture.".
* `get_amount_inside`: Takes another shape (square or rectangle) as an argument. Returns 
the number of times the passed in shape could fit inside the shape (with no rotations). 

Additionally, if an instance of a `Rectangle` is represented as a string, it looks
like: `Rectangle(width=5, height=10)`

The `Square` class is a subclass of `Rectangle`. 

### Example :

Usage example:
```py    
    rect = shape_calculator.Rectangle(10, 5)
    print(rect.get_area())
    rect.set_height(3)
    print(rect.get_perimeter())
    print(rect)
    print(rect.get_picture())
 
    sq = shape_calculator.Square(9)
    print(sq.get_area())
    sq.set_side(4)
    print(sq.get_diagonal())
    print(sq)
    print(sq.get_picture())
 
    rect.set_height(8)
    rect.set_width(16)
    print(rect.get_amount_inside(sq))
```    

That code should return:
```
    50
    26
    Rectangle(width=10, height=3)
    **********
    **********
    **********

    81
    5.656854249492381
    Square(side=4)
    ****
    ****
    ****
    ****

    8
	```