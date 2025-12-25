import pygame
import sys
import pyperclip
import matplotlib.pyplot as plt
from Lost import list_day, list_eu, list_us, list_cn
from Config import width, height, WHITE, BLUE, LIGHT_BLUE, BLACK, button_x, button_y, button_width, button_height, text_x, text_y, text_width, text_height, start, currencies, gap_x, gap_y

pygame.init()

font = pygame.font.Font(None, 40)
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("Курс Валют 1.1")

btn1 = True
user_text = ''
text1 = False 
currency1 = False
files_count = 0
chosen_currency = ''
search_text = ''
found_files = []
currency_boolean = False

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.MOUSEBUTTONDOWN:
            if btn1 == True:
                mouse_x, mouse_y = pygame.mouse.get_pos()
                if (button_x <= mouse_x <= button_x + button_width and
                    button_y <= mouse_y <= button_y + button_height):
                    btn1 = False
                    text1 = True
            else:
                mouse_x, mouse_y = pygame.mouse.get_pos()
                if (start <= mouse_x <= width - start and
                    start <= mouse_y <= y_position):
                        chosen_currency = currencies[(mouse_y - start) // text_height]
                        if chosen_currency == 'EUR':
                            plot_currency = list_eu
                        elif chosen_currency == 'USD':
                            plot_currency = list_us
                        elif chosen_currency == 'CNY':
                            plot_currency = list_cn
                        if user_text == '':                           
                            plt.figure(figsize=(20, 2.7))
                            plt.plot(list_day, plot_currency, label=chosen_currency, marker='o', linewidth = 2)
                            manager_eu = plt.get_current_fig_manager()
                            manager_eu.window.move(0, 0)
                            plt.title('Курс ' + chosen_currency, fontsize = 18)
                            plt.xlabel('Дни', fontsize = 14)
                            plt.ylabel('Рубли', fontsize = 14)
                            plt.legend()
                            plt.grid(True, alpha = 0.4)
                            plt.tight_layout()
                            plt.show()
                        else:
                            for days in range(len(list_day)):
                                if user_text == list_day[days]:
                                    day_text = user_text
                                    currency_boolean = True
        elif event.type == pygame.KEYDOWN:
            if text1 == True:
                if event.key == pygame.K_DELETE:
                    user_text = ""
                elif event.key == pygame.K_BACKSPACE:
                    user_text = user_text[:-1]
                elif event.key == pygame.K_LCTRL:
                    user_text = user_text + pyperclip.paste()
                else:
                    user_text += event.unicode      

    screen.fill(WHITE)
    if btn1 == True:
        button_color = LIGHT_BLUE if pygame.mouse.get_pos()[0] in range(button_x, button_x + button_width) and \
                                      pygame.mouse.get_pos()[1] in range(button_y, button_y + button_height) else BLUE
        pygame.draw.rect(screen, button_color, (button_x, button_y, button_width, button_height))
        text = font.render("Начать работу", True, WHITE)
        text_rect = text.get_rect(center=(button_x + button_width // 2, button_y + button_height // 2))
        screen.blit(text, text_rect)
    if text1 == True:
        y_position = 20
        for currency in currencies:
                text_surface1 = font.render(currency, True, BLACK)
                screen.blit(text_surface1, (text_x, y_position))
                y_position += text_height
        pygame.draw.rect(screen, BLACK, (text_x, text_y, text_width, text_height), 2)
        if currency_boolean == True:
            currency_text = 'Курс 1 ' + chosen_currency + ' ' + day_text + ' = ' + str(plot_currency[days]) + ' RUB'
            text_currency = font.render(currency_text, True, BLACK)
            screen.blit(text_currency, (text_x, text_y - text_height))
        text_surface2 = font.render(user_text, True, BLACK)
        screen.blit(text_surface2, (text_x + gap_x, text_y + gap_y))
        add_text = font.render('Выберете дату и нажмите на валюту', True, BLACK) 
        screen.blit(add_text, (text_x + gap_x, text_y + text_height + gap_y))
        add2_text = font.render('Удалить этот текст можно нажав Delete', True, BLACK)
        screen.blit(add2_text, (text_x + gap_x, text_y + 2 * text_height + gap_y))
        add3_text = font.render('Можно вставить текст нажав LCtrl', True, BLACK)
        screen.blit(add3_text, (text_x + gap_x, text_y + 3 * text_height + gap_y))
        add4_text = font.render('Если оставить поле пустым и нажать на валюту, то откроется её курс за последние недели', True, BLACK)
        screen.blit(add4_text, (text_x + gap_x, text_y + 4 * text_height + gap_y))
        
    pygame.display.flip()

pygame.quit()
sys.exit()
