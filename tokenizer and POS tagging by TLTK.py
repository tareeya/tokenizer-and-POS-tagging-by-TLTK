!pip install tltk
from google.colab import drive
drive.mount('/content/drive')
import tltk
import os

!ls /content/drive/My\ Drive


folder_path = ''
new_folder_path = ''


if not os.path.exists(new_folder_path):
    os.makedirs(new_folder_path)


def pos_tagging(text):
    return tltk.nlp.pos_tag(text)


file_counter = 0
for file_name in os.listdir(folder_path):
    if file_name.endswith('.txt'):
        file_path = os.path.join(folder_path, file_name)


        with open(file_path, 'r', encoding='utf-8') as file:
            text = file.read()


        tagged_text = pos_tagging(text)
        print('Tagging', file_name)


        new_file_name = file_name.replace('.txt', '_tagged.conllu')
        new_file_path = os.path.join(new_folder_path, new_file_name)


        with open(new_file_path, 'w', encoding='utf-8') as conll_file:
            global_word_counter = 1
            sentence_counter = 1
            for sentence in tagged_text:
                conll_file.write(f"# Sentence {sentence_counter}\n")
                for word_pos_pair in sentence:
                    word = word_pos_pair[0]
                    pos = word_pos_pair[1]


                    conll_file.write(
                        f"{global_word_counter}\t{word}\t_\t{pos}\t_\t_\t0\t_\t_\t_\n"
                    )
                    global_word_counter += 1
                conll_file.write("\n")
                sentence_counter += 1
            file_counter += 1
            print('บันทึกไฟล์ลำดับที่', file_counter, 'เรียบร้อย')

print('POS tagging completed and files are saved in the new folder as CoNLL-U files.')