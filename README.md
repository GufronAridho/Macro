# COPYRIGHT NOTICE

This is the work of Bill Byrne, Karthik Krishnamoorthi, Saravanan Ganesh, Amit Dubey, Kyu-Young Kim and Andy Cedilnik from Google LLC, made available under the Creative Commons Attribution 4.0 License. A full copy of the license can be found at https://creativecommons.org/licenses/by/4.0/

## STRUCTURE
Each conversation in the data file has the following structure:
* __conversation_id:__ A universally unique identifier with the prefix 'dlg-'. The ID has no meaning.
* __utterances:__ An array of utterances that make up the conversation.
* __instruction_id:__ A reference to the file(s) containing the user (and, if applicable, agent) instructions for this conversation.

Each utterance has the following fields:
* __index:__ A 0-based index indicating the order of the utterances in the conversation.
* __speaker:__ Either USER or ASSISTANT, indicating which role generated this utterance.
* __text:__ The raw text of the utterance. 'ASSISTANT' turns are originally written (then played to the user via TTS) and 'USER' turns are transcribed from the spoken recordings of crowdsourced workers.
* __segments:__ An array of various text spans with semantic annotations.

Each segment has the following fields:
* __start_index:__ The position of the start of the annotation in the utterance text.
* __end_index:__ The position of the end of the annotation in the utterance text.
* __text:__ The raw text that has been annotated.
* __annotations:__ An array of annotation details for this segment.

Each annotation has a single field:
* __name:__ The annotation name.
