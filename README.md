
<h2>To-Do Requirements:</h2>

<ol>
    <li>Need to pass each venueID in an array and get location of the venue from the HTML. done & optimized</li>
    <li>Slice the LonLat and store in a var. done & optimized</li>
    <li>Pass the vars in a loop to reverse_geocoder. done</li>
    <li>Get results and append to the fullCourts array in related dictionary index. done & optimized</li>
    <ol>
        <li>Result1: Duration from Origin (currently hardcoded Qortuba)</li>
        <li>Result2: City (pass into isValid to only get English results and cities not governates). done & optimized</li>
    </ol>
<li>Get prices from another loop.</li>
<li>Validate in each run if list is up to date by checking count existing and actual count</li>
<li>If the venue does not exist look it up and run the whole process to append it to the full array (textFile)</li>
</ol>

<h2>Bugs:</h2>
<ul>
<li>Ignoring size of the venue</li>
<li>VenueIDs are for the parent venue and not the child (subnames)</li>
</ul>
