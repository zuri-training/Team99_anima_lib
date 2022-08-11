//Creating an object called anima which holds all the animation methods available
//to the user
const anima = {
  //UP ANIMATION
  moveUp: function (id, duration, iterations = 1) {
    document.getElementById(id).animate([{ transform: "translateY(-2em)" }], {
      duration: duration,
      iterations: iterations,
      direction: "alternate",
      easing: "ease-in-out",
    });
  },

  //DOWN ANIMATION
  moveDown: function (id, duration, iterations = 1) {
    document.getElementById(id).animate([{ transform: "translateY(2em)" }], {
      duration: duration,
      iterations: iterations,
      direction: "alternate",
      easing: "ease-in-out",
    });
  },

  //LEFT ANIMATION
  moveLeft: function (id, duration, iterations = 1) {
    document.getElementById(id).animate([{ transform: "translateX(-4em)" }], {
      duration: duration,
      iterations: iterations,
      direction: "alternate",
      easing: "ease-in-out",
    });
  },

  //RIGHT ANIMATION
  moveRight: function (id, duration, iterations = 1) {
    document.getElementById(id).animate([{ transform: "translateX(4em)" }], {
      duration: duration,
      iterations: iterations,
      direction: "alternate",
      easing: "ease-in-out",
    });
  },

  //BOUNCE ANIMATION
  bounce: function (id, duration, iterations = 1) {
    document
      .getElementById(id)
      .animate(
        [{ transform: "translateY(-1em)" }, { transform: "translateY(1em)" }],
        {
          duration: duration,
          iterations: iterations,
          direction: "alternate",
          // easing:'ease-in-out',
        }
      );
  },

  //FADE-IN ANIMATION
  fadeIn: function (id, duration, iterations = 1) {
    document
      .getElementById(id)
      .animate([{ opacity: 0.2 }, { transform: "translateX(-2em)" }], {
        duration: duration,
        iterations: iterations,
        // direction: "alternate",
        easing: "ease-in-out",
      });
  },

  //FADE-OUT ANIMATION
  fadeOut: function (id, duration, iterations = 1) {
    document
      .getElementById(id)
      .animate([{ transform: "translateX(-2em)" }, { opacity: 0.2 }], {
        duration: duration,
        iterations: iterations,
        // direction: "alternate",
        easing: "ease-in-out",
      });
  },

  //BLINK ANIMATION
  blink: function (id, duration, iterations = 1) {
    document
      .getElementById(id)
      .animate([{ opacity: 0 }, { opacity: 0.5 }, { opacity: 1 }], {
        duration: duration,
        iterations: iterations,
        // direction: "alternate",
        easing: "ease-in-out",
      });
  },
  //ROTATE ANIMATION
  rotate: function (id, duration, iterations = 1) {
    document.getElementById(id).animate(
      [
        { transform: "rotate(0) translate3D(-50%, -50%, 0)" },
        {
          transform: "rotate(360deg) translate3D(-50%, -50%, 0)",
        },
      ],
      {
        duration: duration,
        iterations: iterations,
        // direction: "alternate",
        // easing: "ease-in-out",
      }
    );
  },
  // SHAKE FUNCTION
  shake: function (id, duration, iterations = 1) {
    document
      .getElementById(id)
      .animate(
        [
          { transform: "translate(1px, 1px) rotate(0deg)" },
          { transform: "translate(-1px, -2px) rotate(-1deg)" },
          { transform: "translate(-3px, 0px) rotate(1deg)" },
          { transform: "translate(3px, 2px) rotate(0deg)" },
          { transform: "translate(1px, -1px) rotate(1deg)" },
          { transform: "translate(-1px, 2px) rotate(-1deg)" },
          { transform: "translate(-3px, 1px) rotate(0deg)" },
          { transform: "translate(3px, 1px) rotate(-1deg)" },
          { transform: "translate(-1px, -1px) rotate(1deg)" },
          { transform: "translate(1px, 2px) rotate(0deg)" },
          { transform: "translate(1px, -2px) rotate(-1deg)" },
        ],
        {
          duration: duration,
          iterations: iterations,
        }
      );
  },
  //FLIP ANIMATION
  flip: function (id, duration, iterations=1) {
    document.getElementById(id).animate([{ transform: "rotateY(360deg)" }], {
      duration: duration,
      iterations: iterations,
      // direction: "alternate",
      // easing: "ease-in-out",
    });
  },

  //PULSE ANIMATION
  pulse: function (id, duration, iterations=1) {
    document.getElementById(id).animate([{ transform: "scale(0.5)" }], {
      duration: duration,
      iterations: iterations,
      // direction: "alternate",
      // easing: "ease-in-out",
    });
  },
  
  //SLIDE ANIMATION
  slide: function (id, duration, iterations=1) {
    document.getElementById(id).animate(
      [
        {
          transform: "translateX(0px)",
        },
        {
          transform: "translateX(500px)",
        },
      ],
      {
        duration: duration,
        iterations: iterations,
        direction: "alternate",
        easing: "ease-in-out",
      }
    );
  },
  
};

// Testing the animation methods
// anima.shake("black", 500, 7);
