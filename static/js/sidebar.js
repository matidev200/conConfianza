$(".logo").on('click', function () {
    if($('aside').is(':hidden')){
        $("aside").show()
      } else {
        $("aside").hide()
      }
})