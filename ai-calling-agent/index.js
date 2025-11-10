require('dotenv').config();
const express = require('express');
const bodyParser = require('body-parser');
const twilio = require('twilio');
const fs = require('fs');

const app = express();
app.use(bodyParser.urlencoded({ extended: false }));
app.use(bodyParser.json());

const client = twilio(process.env.TWILIO_ACCOUNT_SID, process.env.TWILIO_AUTH_TOKEN);

app.get('/', (req, res) => {
  res.send(' AI Calling Agent Server is Running');
});


app.post('/make-call', async (req, res) => {
  try {
    const call = await client.calls.create({
      to: '+916363107451',
      from: process.env.TWILIO_PHONE_NUMBER,
     
      url: `${process.env.NGROK_URL}/voice`
    });
    console.log(' Call initiated! SID:', call.sid);
    res.json({ message: 'Call started!', callSid: call.sid });
  } catch (err) {
    console.error(' Error making call:', err);
    res.status(500).json({ error: err.message });
  }
});


app.post('/voice', (req, res) => {
  const VoiceResponse = twilio.twiml.VoiceResponse;
  const twiml = new VoiceResponse();


  twiml.say('Hello, this is Sukruth’s AI Calling Agent. This call will now be recorded for demo purposes.');


  twiml.record({
    recordingStatusCallback: '/recording-status',
    recordingStatusCallbackMethod: 'POST',
    playBeep: true,
    maxLength: 30
  });

  twiml.hangup();

 
  res.type('text/xml');
  res.send(twiml.toString());
});



app.post('/recording-status', (req, res) => {
  const recordingUrl = req.body.RecordingUrl;
  const callSid = req.body.CallSid;
  console.log(`🎧 Recording saved for call ${callSid}: ${recordingUrl}`);


  fs.appendFileSync('recordings.txt', `${new Date().toISOString()} | ${callSid} | ${recordingUrl}\n`);

  res.status(200).send('OK');
});

app.listen(process.env.PORT || 3000, () => {
  console.log(`Server running on port ${process.env.PORT}`);
});
