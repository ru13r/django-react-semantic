
// Semantic-ui imports
import 'semantic-ui-css/semantic.min.css';
import 'semantic-ui-css/semantic.min.js'
import 'semantic-ui-css/components/form'
import 'semantic-ui-css/components/visibility'
import 'semantic-ui-css/components/transition'
import 'semantic-ui-css/components/sidebar'

// local CSS imports
import '../stylesheets/semantic-base.css'
import '../stylesheets/base'

// Semantic fix menu plugin
$(document)
    .ready(function () {

        // fix menu when passed
        $('.masthead, .top-navigation')
            .visibility({
                once: false,
                onBottomPassed: function () {
                    $('.fixed.menu').transition('fade in');
                },
                onBottomPassedReverse: function () {
                    $('.fixed.menu').transition('fade out');
                }
            })
        ;

        // create sidebar and attach to menu open
        $('.ui.sidebar')
            .sidebar('attach events', '.toc.item')
        ;

    });