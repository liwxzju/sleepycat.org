function replyto(id, user)
{
    document.getElementById("reply_to_user").innerHTML = "回复：<span style='color:#2099AB; font-weight: bold;'>" + user + "</span>&nbsp;<a href='#reply_to_user' onclick='cancelreply()' style='color: #BABABA;text-decoration: none;'>(撤消)</a>";
    document.getElementById("reply_to_comment").value = id;
}

function cancelreply()
{
    document.getElementById("reply_to_user").innerHTML = "";
    document.getElementById("reply_to_comment").value = "";
}