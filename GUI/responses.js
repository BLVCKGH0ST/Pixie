function getBotResponse(input) {
    
    if (input == "i want to open an account") {
        return "What type of account do you want to open";
    } else if (input == "i want to transfer money") {
        return "Provide the Recievers Number and Name";
    } else if (input == "i want to see my bank statement") {
        return "Word you want to recieve it by mail or by text?";
    } else if ( input =="by mail") {
        return "the bank statement will be sent to the email connected to your bank account";
    }else if ( input == "by text"){
        return "your statement will be prepared soon and sent to the number connected to your bank account";
    }if (input == "savings account"){
        return " provide your first name and last name and passport/national card number";
    } else if (input == "i would like to schedule a transfer") {
        return "Provide the receivers name,number and the time you want the transfer to be made";
    }

    // Simple responses
    if (input == "hello") {
        return "Hello there!";
    } else if (input == "goodbye") {
        return "Hope the information was helpful.Goodbye!!";
    } else {
        return "Kindly rephrase the question!";
    }
}
