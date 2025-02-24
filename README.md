In this project, I have simulated the formation of Rock Candy using Random Walk and the principles of Thermodynamics.

To begin, we must first ask ourselves, "How is Rock Candy made?" The simplified process is as follows:

1-    Prepare a large container filled with hot water.
2-    Add sugar to the container to create a supersaturated solution.
3-    Place a stick in the center of the container.
4-    Gradually cool the solution.

Now that we understand how Rock Candy is made, we can simulate the process.

In this program, I assumed that the container consists of several parallel 2D plates placed vertically on top of one another. Sugar molecules move freely within each plate, following a Random Walk. If a molecule reaches the stick (represented as a red circle in the center of the plate), it stops moving. Additionally, if a molecule moves to a neighboring point of a static molecule, it also becomes static.

To determine the number of sugar molecules in each plate, I assumed their distribution follows Boltzmann's distribution due to the effect of gravity.

By integrating these components, I first solved the problem for a single 2D plate and then extended the solution to other 2D plates. Finally, I stacked these plates to construct a 3D representation of the Rock Candy formation.

I hope you enjoy watching this simulation! If you have any suggestions, please feel free to contact me. :)

![Screenshot from 2025-02-24 13-55-49](https://github.com/user-attachments/assets/e998f8cd-5524-4446-b77f-afdbcebbca3b)
