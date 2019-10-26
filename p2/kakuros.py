from __future__ import absolute_import
from __future__ import division
from __future__ import print_function
from ortools.sat.python import cp_model

def Function(Operation):
    # Creates the model.
    model = cp_model.CpModel()

    # Creates the variables.

    x1 = model.NewIntVar(0, 9, 'x1')
    x2 = model.NewIntVar(0, 9, 'x2')
    x3 = model.NewIntVar(0, 9, 'x3')

    y1 = model.NewIntVar(0, 9, 'y1')
    y2 = model.NewIntVar(0, 9, 'y2')
    y3 = model.NewIntVar(0, 9, 'y3')

    z1 = model.NewIntVar(0, 9, 'z1')
    z2 = model.NewIntVar(0, 9, 'z2')
    z3 = model.NewIntVar(0, 9, 'z3')

    model.Add((x1 + y1 + z1) == Operation[0])
    model.Add((x2 + y2 + z2) == Operation[1])
    model.Add((x3 + y3 + z3) == Operation[2])
    model.Add((x1 + x2 + x3) == Operation[3])
    model.Add((y1 + y2 + y3) == Operation[4])
    model.Add((z1 + z2 + z3) == Operation[5])

    # Create List For Rows
    Row1=[x1,x2,x3]
    Row2=[y1,y2,y3]
    Row3=[z1,z2,z3]
    # Create List For Columns
    Column1=[x1,y1,z1]
    Column2=[x2,y2,z2]
    Column3=[x3,y3,z3]
    # Creates the constraints.

    model.AddAllDifferent(Row1)
    model.AddAllDifferent(Row2)
    model.AddAllDifferent(Row3)

    model.AddAllDifferent(Column1)
    model.AddAllDifferent(Column2)
    model.AddAllDifferent(Column3)
    # Creates a solver and solves the model.
    solver = cp_model.CpSolver()
    status = solver.Solve(model)

    if status == cp_model.FEASIBLE:
            outputFile.write("x" + ", " + str(Numbers[0]) + ", " + str(Numbers[1]) + ", " + str(Numbers[2]) + "\n" +
                                          str(Numbers[3]) + ", " + str(solver.Value(x1)) + ", " + str(solver.Value(x2)) + ", " + str(solver.Value(x3)) + "\n" +
                                          str(Numbers[4]) + ", " + str(solver.Value(y1)) + ", " + str(solver.Value(y2)) + ", " + str(solver.Value(y3)) + "\n" +
                                          str(Numbers[5]) + ", " + str(solver.Value(z1)) + ", " + str(solver.Value(z2)) + ", " + str(solver.Value(z3)) )

with open("kakuro_input.txt", "r") as inputFile:
    Numbers = []
    for line in inputFile.readlines():
        line = line.strip().split(",")
        for item in line:
            Numbers.append(int(item))

outputFile = open("Kakuro_output.txt", "w")        
Function(Numbers)