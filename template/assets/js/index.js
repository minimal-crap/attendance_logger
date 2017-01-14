var web_socket_url = "ws://localhost:8001/get_attendance_data/";
var data_set = [];
var table_columns = [
            {title:"id"},
            {title:"name"},
            {title:"designation"},
            {title:"department"},
            {title:"check-in time"}
           ];
$(document).ready(function(){
    var ws = new WebSocket(web_socket_url);
    console.log("testing");

    ws.onmessage = function(event){
        //logic to process incoming push messages
        //goes here
        console.log(event.data);
    };

    $("#attendance-live-table").DataTable({
        data: data_set,
        columns: table_columns});
});