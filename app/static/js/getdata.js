var sql = require('mssql'); 

var config = {
    user: 'PokeAdmin@pokestats',
    password: 'P0k3m0ns',
    server: 'pokestats.database.windows.net', // You can use 'localhost\\instance' to connect to named instance 
    database: 'PokeStatsDB',

    options: {
        encrypt: true // Use this if you're on Windows Azure 
    }
}

var connection = new sql.Connection(config, function(err) {
    // ... error checks 
    
    // Query 
    
    var request = new sql.Request(connection); // or: var request = connection.request(); 
    request.query('select 1 as number', function(err, recordset) {
        // ... error checks 
        
        console.dir(recordset);
    });
    
    // Stored Procedure 
    
    var request = new sql.Request(connection);
    request.input('input_parameter', sql.Int, 10);
    request.output('output_parameter', sql.VarChar(50));
    request.execute('procedure_name', function(err, recordsets, returnValue) {
        // ... error checks 
        
        console.dir(recordsets);
    });
});
 
connection.on('error', function(err) {
    // ... error handler 
});



