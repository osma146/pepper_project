// File: home11/html/js/tag.js
var tags = ['I', 'R2D2', 'a lot', 'accompany', 'affirmative', 'afflicted', 'afford', 'agitated', 
  'alienated', 'all', 'allright', 'alone', 'alright', 'ambitious', 'amused', 'angry', 'anguished', 'anxious', 
  'any', 'apology', 'appease', 'applauds', 'applause', 'arm', 'arrogant', 'ashamed', 'assuage', 'assured', 
  'astonishment', 'attack', 'attemper', 'attention', 'avoid', 'back', 'back rubs', 'bad', 'bandmaster', 'bashful', 
  'beat', 'becalm', 'beg', 'beseech', 'bewilder', 'binoculars', 'bird', 'birthday', 'blank', 'blind', 
  'body language', 'bored', 'bow', 'bowing', 'breath', 'bug', 'but', 'call', 'call a taxi', 'calm', 
  'camera', 'capture', 'car', 'care', 'careerist', 'cautious', 'choice', 'choose', 'chopper', 'clear', 
  'cloud', 'cogitate', 'collude', 'color', 'come on', 'conceited', 'concern', 'conductor', 'confident', 'confused', 
  'conspire', 'continue', 'cool', 'copter', 'count', 'coward', 'crazy', 'crouch', 'cry', 'curious', 
  'curl', 'dance', 'dazzled', 'decided', 'demur', 'deploy', 'depressed', 'despairing', 'desperate', 'determined', 
  'detestation', 'disappointed', 'discouraged', 'distrustful', 'dizzy', 'doubt', 'down', 'drink', 'drive', 'droid', 
  'dumbbells', 'earth', 'ecstatic', 'edgy', 'embarrassed', 'empty', 'emulate', 'enthusiastic', 'entire', 'entreat', 
  'estimate', 'ethernet', 'evening', 'every', 'everyone', 'everything', 'exalted', 'examine', 'except', 'excited', 
  'excuse', 'exhausted', 'explain', 'far', 'fear', 'fearful', 'felled', 'field', 'fierce', 'fight', 
  'fitness', 'five', 'flash', 'floor', 'fly', 'follow', 'forlorn', 'four', 'friendly', 'frightened', 
  'front', 'frustrated', 'furious', 'gentle', 'get', 'gift', 'give', 'go', 'gorilla', 'gosh', 
  'great', 'ground', 'grunt', 'guiltless', 'guitar', 'hand', 'happy', 'harmful', 'hate', 'hatred', 
  'haughty', 'head', 'heat', 'heaven', 'helicopter', 'hello', 'her', 'here', 'hesitate', 'hesitation', 
  'hey', 'hi', 'hide', 'hide eyes', 'hide hands', 'high', 'him', 'hit', 'hopeful', 'hopeless', 
  'hot', 'hound', 'hum', 'humiliated', 'hungry', 'hurt', 'hysterical', 'imitation', 'implore', 'impressed', 
  'incomprehension', 'indicate', 'innocent', 'inquisitive', 'insane', 'interested', 'intriguing', 'irritated', 'isolated', 'joke', 
  'joker', 'joy', 'joyful', 'karate', 'keen', 'kiss', 'knight', 'knock', 'knock eye', 'kung fu', 
  'late', 'laugh', 'lead', 'leader', 'leave', 'light', 'lonely', 'look', 'look hand', 'loop', 
  'lost', 'love you', 'lunatic', 'mad', 'magic', 'malignant', 'martial art', 'maybe', 'me', 'meditate', 
  'mime', 'mimic', 'mischievous', 'mistrustful', 'mock', 'modest', 'mollify', 'monitor', 'monster', 'more', 
  'muscle', 'music', 'musician', 'my', 'myself', 'mystical', 'negative', 'nervous', 'nervousness', 'nervy', 
  'next', 'night', 'no', 'nosy', 'not know', 'not me', 'nothing', 'object', 'observe', 'obstinate', 
  'odium', 'off', 'offer', 'ok', 'on', 'once upon a time', 'one', 'oppose', 'optimistic', 'or', 
  'orchestra', 'other', 'ouch', 'pacify', 'pain', 'palm', 'party', 'peaceful', 'pensive', 'perhaps', 
  'persistent', 'phew', 'photo', 'pick', 'picture', 'placate', 'place', 'plane', 'play', 'play with hands', 
  'please', 'plug', 'power', 'prayer', 'present', 'proffer', 'protect', 'protest', 'proud', 'psst', 
  'puzzled', 'puzzling', 'quiet', 'rapturous', 'raring', 'reason', 'refute', 'reject', 'relaxation', 'relieved', 
  'repressed', 'reserved', 'resolved', 'rest', 'robot', 'rock', 'rousing', 'sad', 'salute', 'say', 
  'scared', 'scheme', 'scratch back', 'scratch bottom', 'scratch eye', 'scratch hand', 'scratch head', 'scratch leg', 'scratch torso', 
  'see', 'see something', 'seize', 'select', 'servant', 'shake', 'shamefaced', 'shine', 'shocked', 'show', 
  'show muscles', 'show sky', 'shuttle', 'shy', 'sing', 'single', 'sky', 'smell good', 'sneeze', 'something', 
  'song', 'soothe', 'sorry', 'space', 'speak', 'sport', 'starship', 'steal', 'stop', 'stretch', 
  'stroke', 'strong', 'stubborn', 'stupor', 'subtract', 'sun', 'supplicate', 'sure', 'surprise', 'surprised', 
  'suspicious', 'sword', 'tablet', 'take', 'talk', 'tall', 'taxi', 'that', 'them', 'there', 
  'these', 'think', 'thinking', 'this', 'thoughtful', 'three', 'timid', 'tired', 'top', 'touch', 
  'train', 'two', 'unacquainted', 'uncomfortable', 'undead', 'understand', 'undetermined', 'undiscovered', 'unfamiliar', 'unknown', 
  'unless', 'unplug', 'up', 'upbeat', 'upstairs', 'vexed', 'victory', 'vision', 'void', 'waddle', 
  'wait', 'wake up', 'warm', 'watch', 'waw', 'weird', "what's this", 'whew', 'whisper', 'whistle', 
  'wicked', 'wickedness', 'wild', 'win', 'wing', 'winner', 'worn', 'worried', 'worry', 'yeah', 
  'yes', 'yoo-hoo', 'you', 'your', 'yum', 'zero', 'zestful', 'zombie'];

var grid = document.getElementById("button-grid");

for (var i = 0; i < tags.length; i++) {
  var tag = tags[i];

  var div = document.createElement("div");
  div.className = "grid-item2";

  var btn = document.createElement("button");
  btn.className = "square-btn2";
  btn.innerText = tag;

  // Use classic function instead of arrow
  btn.onclick = (function(t) {
    return function() {
      sendMessage({ "type": "tag", "tag": t });
      //alert(t)
    };
  })(tag);

  div.appendChild(btn);
  grid.appendChild(div);
}
