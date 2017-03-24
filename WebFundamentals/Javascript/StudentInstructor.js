var users = {
'Students': [
   {first_name:  'Michael', last_name : 'Jordan'},
   {first_name : 'John', last_name : 'Rosales'},
   {first_name : 'Mark', last_name : 'Guillen'},
   {first_name : 'KB', last_name : 'Tonel'}
],
'Instructors': [
   {first_name : 'Michael', last_name : 'Choi'},
   {first_name : 'Martin', last_name : 'Puryear'}
]
}
function dictionary(users){
 var count=1,length=0;
 for(var key in users)
 {
     console.log(key);
     for(var key1 in users[key])
         {
           length=users[key][key1].first_name.length+users[key][key1].last_name.length;
           console.log(count+" - "+users[key][key1].first_name+" "+users[key][key1].last_name+" - "+length);
           count++;
         }
    }
}
dictionary(users);
