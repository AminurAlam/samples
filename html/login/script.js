const passwords = {
  aa: "aa",
  ss: "ss",
  dd: "dd",
  ff: "ff",
};

function signup() {
  // var un = username.value;
  // var pass = password.value;
  // var dob = dob.value;
  // var email = email.value;
  if (!username.value.match(/^\w+$/)) {
    console.log("un nahh");
    return;
  }
  if (password.value.length < 8) {
    console.log("pass is too short");
    return;
  }
  // if (!dob.value.match(/^\w+$/)) {
  //   console.log("un nahh");
  //   return;
  // }
  if (!username.value.match(/^\w+$/)) {
    console.log("un nahh");
    return;
  }
  console.log("step right up");
}

function login() {
  var un = username.value;
  var pass = password.value;

  if (un in passwords) {
    if (passwords[un] == pass) {
      window.location = `/user/${un}`;
    } else {
      window.alert("wrong password!!");
    }
  } else {
    window.alert(`username ${un} not found!!`);
  }
}
