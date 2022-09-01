$('.carousel').carousel({
    interval: 5000
  });

  var myVar;
  function myFunction() {
    myVar = setTimeout(showPage, 3000);
    document.body.style.backgroundColor = "#0e1014";
  }
  function showPage() {
    document.getElementById("Myloader").style.display = "none";
    document.getElementById("preloader").style.display = "block";
  };
  
  $('#mydegoo').click(function () {
    var Email = $('#Email').val('savantinfolabs@gmail.com');
    var password = $('#password').val('t!R@tSh12#');
    window.location.href = '@Url.Action("https://analytics.google.com/g/collect?v=2&tid=G-668MSHBNLB&gtm=2oe8o0&_p=2020892791&cid=1321992198.1661685844&ul=en-in&sr=1536x864&_z=ccd.v9B&sid=1661793098&sct=4&seg=1&dl=https%3A%2F%2Fapp.degoo.com%2Ffiles%2F0&dr=https%3A%2F%2Fapp.degoo.com%2F&dt=Degoo%20Cloud&_s=1")';
});