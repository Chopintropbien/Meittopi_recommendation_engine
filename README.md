REST API:
=========

Specifications can be found in the API_specs.md file

TODO and roadmap:
=================



Standard IO as a back-end DB
----------------------------
 * TODO: add login for the server used to serve the javascript and other user-side content

Recommendations
----------------
the idea to run the recommendation is the following:
    - fragment the review into the smaller parts
    - for each smaller part, project it into a field of "important features"
    - determine sentiment and polarization => project into an appropriate space
    - Run spectral clustering and fragment
        - reviews in the most look-like
        - restaurants into the most look-like
        - persons into the most look-like
    -account for assymetric matching:
        - if one restaurant is definetely better then an another one in all perspectives
        - if one of the reviewers has definetely a better ability to review then all the
            others.


To check with Lauriane
-----------------------

 * Do we do identification via FB for the users and redirection towards the official restaurant page for the restaurant?
 * If yes, what should be stored?
 * Should we contract user images into their profile to start with? => managing default image? // mongoDB slice?
 * Do we need to do a pseudo lock once the availability has been checked?
 * Should I specify the user modification (relations included) by the HTML POST requests or by accessing specific APIs with a POST?
 (it looks like the first option is preferable); this will avoid us to