(function($) {
  $(function() {
    function toggleTimelineSource() {
      var timeline_source = $('input[name="timeline_source"]:checked').val();
      $('.field-search_query, .field-screen_name').removeClass('required').hide();

      if (timeline_source == 'user' || timeline_source == 'favorites') {
        $('.field-screen_name').show();
      } else if (timeline_source == 'search') {
        $('.field-search_query').addClass('required').show();
      }
    }

    toggleTimelineSource();

    $('input[name="timeline_source"]').change(function() {
      toggleTimelineSource();
    });
  });
})(django.jQuery);
