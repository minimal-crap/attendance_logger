var web_socket_url = "ws://localhost:8002/get_attendance_data";
var data_set = [];
var table_columns = [];
$(document).ready(function(){
    var ws = WebSocket(web_socket_url);

    ws.onmessage = function(even){
        //logic to process incoming push messages
        //goes here
    };

    $("#attendance-live-table").DataTable(
        data: data_set;
        columns: table_columns;
    );
});