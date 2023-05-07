# Create IsoCam

“Creates a true isometric camera or a isometric camera for game needs”

![07 05 2023_15 37 49_REC](https://user-images.githubusercontent.com/69900896/236664596-6b5a5e19-4553-4d13-993c-2853ed891e6f.gif)

Create Isocam creates an orthographic camera with which you can render isometric views.

- A camera setup for true mathematical isometric
- A camera setup with a view that is needed to render traditional isometric graphics for a 2D game with a ratio of 2 to 1
- A camera setup to render a special game iso format with a ratio of 4 to 3

### ****TrueIsocam****

![image](https://user-images.githubusercontent.com/69900896/236663779-c5ecbac0-6b73-4782-a98e-b22de6c1f013.png)

The button with the label TrueIsocam creates a mathematical correct isoview with a flank angle of 30 degrees. This is for example wanted for architectural graphics.

The camera has a rotation of 35.264 degrees. Or 54.736 degrees in Blender.

### ****GameIsocam****

![image](https://user-images.githubusercontent.com/69900896/236663784-bef9d839-0ca7-4224-8c58-dbe87f3ee037.png)

The button with the label GameIsocam creates a camera with a special view that is needed to render isometric graphics for a 2D game. The setup differs a bit from the true iso. The camera for a mathematical correct isometric view doesn’t work for games As you can see at the next shot.

The stairs effect does simply not match together. There are either gaps or overlappings.

The teeth of the borders doesn't sync. So we need a different angle for game needs. And that’s what the GameIsocam is for.

What’s the reason? The first isometric games were pixeled, not rendered. One pixel up, two pixel sidewards. It was also important to have power of two graphics. And this simply leads to another flank angle compared to the true isometric with its 30 degrees.

This is of course then not longer a true isometric view. But a special parallel projection, also called dimetric. But the game world calls it isometric since eons. Maybe because it is pretty close to the real isometric view.

The camera rotation is 30 degrees here, or 60 degrees in Blender. You can render the result as a base tile of 64×32 pixels then.

![image](https://user-images.githubusercontent.com/69900896/236663801-80e5d4a4-9a6c-4b1e-9698-78ac644e25b3.png)

Here the stairs effect fits perfectly together. The teeth goes into each other, without gaps or overlappings. And we have a power of 2 ratio.

### ****GameIso4to3cam****

![image](https://user-images.githubusercontent.com/69900896/236663807-753eda68-24fc-42f4-a4ec-31c5c3b41af1.png)

There is another special view that fits together like the one with the 2:1 ratio . Here we don’t have a basetile of 64×32 and a ratio of 2:1, but one with 64×48 and a ratio of 4:3. It is of course not a power of two graphics anymore. And far away from the true isometric view. But the old graphics card limits are long gone. And when you need a more topdown view, then this is perfect.

For that the camera has a rotation 48.5 Grad, or in Blender a rotation of 41.5 Grad.

### ****Groundplane****

The button Groundplane creates a plane with a size of 10 x 10 Blender units. All three cameras are set up to fit to that groundplane.

### ****Credits****
Initial creator, 2.8 update and bitbucket thread can be found [Blender Artist](https://blenderartists.org/t/create-isocam/603183) and [@jasonicarter](https://github.com/jasonicarter)


****Note: This addon includes an updater, which you can use to keep it up to date within Blender.****
