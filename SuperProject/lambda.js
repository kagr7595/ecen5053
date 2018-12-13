console.log('RPiServer1 function');

var AWS = require('aws-sdk');
//var QUEUE_URL = 'https://sqs.us-east-1.amazonaws.com/918893548996/StandardQueue';
var QUEUE_URL = 'https://sqs.us-east-1.amazonaws.com/918893548996/Fifo_Queue.fifo';
var sqs = new AWS.SQS({region : 'us-east-1'});

exports.handler = function(event, context) {
    
    //Comment lines 11-14 and 30 (while detabbing lines 15-29 to use with non-updated code)
    if(event.alert) {
        //send to cloudwatch (this is the 10 min gate has been opened alert)
        console.log('error:',"Gate has been open for 10 minutes");   
    } else {
        var params1 = {
            MessageBody: JSON.stringify(event),
            QueueUrl: QUEUE_URL,
            MessageGroupId: 'messageGroup1'
        };  
        
        sqs.sendMessage(params1, function(err,data){
            if(err) {
                console.log('error:',"Fail Send Message" + err);
                context.done('error', "ERROR Put SQS");  // ERROR with message
            }else{  
                console.log('data:',data.MessageId);
                context.done(null,'');  // SUCCESS 
            }   
        });
    }
    console.log('Received event:', JSON.stringify(event, null, 2));
    return 0;
};

