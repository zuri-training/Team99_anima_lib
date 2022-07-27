# anima_lib_team99 :trophy:

## Documentation: Animate99 Animation library :space_invader: :technologist:	

### What is Animate99? :grinning:

Animate99 is a JavaScript animation library built for beginner developers. It allows you to easily incorporate animations into your programs without the hassle of writing the code from scratch.
Built into the library is a collection of functions written using normal language (for ease of use) and defined to produce specific animation effects. The developer is also provided with substantial flexibility in how they choose to apply the animations to their code.

### JavaScript vs CSS animations, what’s the difference? :woman_shrugging:

Scripted animations provide greater control and flexibility compared to CSS animations. Animating with CSS  may seem like the easiest way to get something moving on your screen but you will need JavaScript when you need significant control over your animations, because JavaScript doesn’t just provide you with animation functionality, it allows you to easily customize exactly just how you want these animations to behave in your program.  The selling point of the Animate99 library is that it does the heavy lifting of creating customizable and flexible animation functions, all you have to do is sit back and call on them.

### How does it work? :man_teacher:	

Animate99 is built upon the Web Animations API. This API is a native implementation of scripted animations which allows developers to manipulate the animation engine of a browser using nothing else but plain JavaScript, this means developers can have little to no need to utilize multiple libraries in order to create cool animations. 
This also reduces the number of third-party dependencies a program will ultimately have. Another benefit of using JavaScript as the main animation engine is that it aids in maintaining a distinction between behavioral and presentational attributes and this is very important in modern web development.

### Getting started! :rocket:

In order to get started using the Animate99 animation library, you will first need to register as a user on our [website] (www.animate99.com) . Once you are a registered user, you will have access to the library and the option of either embedding/importing the animation library script file.


### Importing Animate99 :computer:
In order to use Animate99, you will need to import the library by adding the library’s script.js file as a script tag to the head tag of your HTML document. To ensure that your other JavaScript files have access to all the animation functions within the library, you need to also make sure that along with the library’s script.js file, all other JavaScript files being used in your program are added as script tags within the head tag of the HTML document.

```
<html>
<head>
    <meta charset="utf-8">
    <meta name="viewport" content="width=device-width, initial-scale=1">
    <title>Home</title>
    <script src="https://animate99.com/script.js" defer></script>
    <script src="index.js" defer></script>
</head>

```
In some cases it may also help to use the defer keyword within the script tags to make sure that you avoid the possibility of console errors when running your program. For more information about the usefulness of the defer keyword and how it can impact the performance of your program check out this [article](https://javascript.info/script-async-defer).
You might also want to avoid using a self closing script tag such as;

```
<script type="text/javascript" src="script.js"/>

```
and instead use opening and closing script tags for your JavaScript files like so;
```
<script src="script.js" defer></script>
```

This will also reduce the chances of running into errors down the line when running your program. 
Once you have added all the relevant script tags to the head tag of your HTML document, you have successfully imported Animate99 and you will have access to all its animation functions. To learn how to apply these functions to your code, check out the ‘Calling and applying specific animation functions’ section of this document.  


### List of available animations :space_invader:
- Move Up
- Move Down
- Move Left
- Move Right
- Bounce
- Shake
- Slide
- Rotate
- Pulse
- Blink
- Fade In
- Fade Out
- Flip

### Calling and executing specific animation functions  ⚛️ :computer:

Once you have successfully imported/ installed the Animate99 library, calling the functions you want to use is the next step. The Animate99 library is stored as  an object called ‘anima’ which contains all the animations available. Each animation function can be called from the library using the following syntax;

```
anima.animationName(id, duration, iterations);
```

For example, you can use the shake animation by calling  the following function and passing in the corresponding arguments that match each parameter;
```
anima.shake(‘myElementId’, 500, 1);
```

It is important to note that when using the animation functions, the animation names should be in lowercase not uppercase, so in the above example, using  ```anima.Shake``` would return an error.

Now that you are clear on the correct syntax to use when calling the animation functions, you might be wondering what the function parameters mean. 

To put it plainly, the **id** parameter represents the id of the element you would like to animate, thus you need to make sure that each element you want to animate has an id assigned to it.

The **duration** parameter (in Milliseconds) represents how fast or slow you would like the animation to run. When no argument is passed in for this parameter, the default value is 500 Ms. By increasing the value of this parameter your animation moves slower. The opposite is the case when you decrease the value.

The **iterations** parameter simply represents how many times you want the animation to repeat. When no argument is passed in for this parameter, the default value is 1.










