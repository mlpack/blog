"use strict";

$(function(){
  var trigger = $("#nav-tags"),
    menu = $("#tag-menu"),
    tagMenuVisible = false,
    isTouch = false;

  function showTagsMenu() {
    if (tagMenuVisible || isTouch)
      return;

    tagMenuVisible = true;
    menu
      .css({
        display: "inline"
      })
      .transition({
        opacity: 1,
        top: "2.2em"
      }, 250);
  }

  function hideTagsMenu() {
    tagMenuVisible = false;
    menu.transition({
      opacity: 0,
      top: "2em"
    }, 250, function() {
      menu.css({
        display: "none"
      });
    });
  }

  trigger.on("touchstart MSPointerOver pointerover", function(event){
    var origEvent = event.originalEvent;
    if (origEvent.pointerType && origEvent.pointerType != 2 && origEvent.pointerType != "touch")
      return;

    // Don't show menu, go to url.
    isTouch = true;
  });

  trigger.on("mouseenter", showTagsMenu);
  $(".navbar").on("mouseleave", hideTagsMenu);
});
