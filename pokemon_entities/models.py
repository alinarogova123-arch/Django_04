from django.db import models


class Pokemon(models.Model):
    title = models.CharField(max_length=200, verbose_name="Название")
    title_en = models.CharField(max_length=200, blank=True, verbose_name="Название на английском")
    title_jp = models.CharField(max_length=200, blank=True, verbose_name="Название на японском")
    description = models.TextField(blank=True, verbose_name="Описание")
    image = models.ImageField(upload_to="images", null=True, verbose_name="Изображение")
    previous_evolution = models.ForeignKey(
    	"self",
    	on_delete=models.CASCADE,
    	blank=True,
    	null=True,
    	related_name="next_evolutions",
    	verbose_name="Предидущая эволюция покемона"
    )

    def __str__(self):
        return f'{self.title}'


class PokemonEntity(models.Model):
	pokemon = models.ForeignKey(Pokemon, on_delete=models.CASCADE, verbose_name="Вид покемона")
	lat = models.FloatField(null=True, verbose_name="Широта")
	lon = models.FloatField(null=True, verbose_name="Долгота")
	appeared_at = models.DateTimeField(null=True, blank=True, verbose_name="Появление")
	disappeared_at = models.DateTimeField(null=True, blank=True, verbose_name="Удаление")
	level = models.IntegerField(null=True, blank=True, verbose_name="Уровень")
	health = models.IntegerField(null=True, blank=True, verbose_name="Здоровье")
	strenght = models.IntegerField(null=True, blank=True, verbose_name="Сила")
	defence = models.IntegerField(null=True, blank=True, verbose_name="Защита")
	stamina = models.IntegerField(null=True, blank=True, verbose_name="Выносливость")
