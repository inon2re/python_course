def PerimeterQuadrilateral(a=0, b=0, c=0, d=0):
    return a+b+c+d
FirstSide, SeccondSide, ThirdSide, FourthSide = int(input('Введите сторону четырехугольника ')), int(input('Введите сторону четырехугольника ')),\
                                                int(input('Введите сторону четырехугольника ')), int(input('Введите сторону четырехугольника ')),

print(PerimeterQuadrilateral(FirstSide, SeccondSide, ThirdSide, FourthSide))