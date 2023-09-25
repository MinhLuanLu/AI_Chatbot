

let imageVisible = false;

function search_click() {
    const searching = 'searching...';
    console.log(searching);
    
    const chatbotIconDiv = document.querySelector('.chatbot_icon_div');
    const inputElement = document.querySelector('.user_input');
    
    
    if (imageVisible) {
        chatbotIconDiv.innerHTML = '';
    } 
    else {
        chatbotIconDiv.innerHTML = '<img class="chatbot_icon" src="Images/chatbot.png">';
    }

    imageVisible = !imageVisible;

    question = []; //Make a emty Array

    diplay_question = question.push(inputElement.value); // add the text to the display_question Array
    document.querySelector('.question_text').innerHTML = inputElement.value;
    inputElement.value = '';

    console.log(question);
    console.log('User Input:', diplay_question);


    const characters_check = question[0].length;
    console.log('Question Characters: ' + characters_check) //Check how many characters in the question list//

    
    
    
    
}

