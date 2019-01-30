from matplotlib import pyplot as plt
import seaborn as sb
current_palette = sb.color_palette()


#Diverging Color Palette
sb.palplot(sb.color_palette("BrBG", 7))

#Sequential Color Palettes
#sb.palplot(sb.color_palette("Greens"))

#Qualitative Color Palettes
#sb.palplot(current_palette)

plt.show()
