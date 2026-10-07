from django.db import models


class Hermano(models.Model):
    """Modelo que representa un hermano con su disponibilidad semanal"""

    nombre = models.CharField(max_length=200, unique=True)
    numero = models.CharField(max_length=20, blank=True, default='')
    comentario = models.TextField(blank=True, default='')

    # Disponibilidad Mañanas - cada día es un booleano
    manana_lunes = models.BooleanField(default=False, verbose_name='Mañana Lunes')
    manana_martes = models.BooleanField(default=False, verbose_name='Mañana Martes')
    manana_miercoles = models.BooleanField(default=False, verbose_name='Mañana Miércoles')
    manana_jueves = models.BooleanField(default=False, verbose_name='Mañana Jueves')
    manana_viernes = models.BooleanField(default=False, verbose_name='Mañana Viernes')
    manana_sabado = models.BooleanField(default=False, verbose_name='Mañana Sábado')
    manana_domingo = models.BooleanField(default=False, verbose_name='Mañana Domingo')

    # Disponibilidad Tardes
    tarde_lunes = models.BooleanField(default=False, verbose_name='Tarde Lunes')
    tarde_martes = models.BooleanField(default=False, verbose_name='Tarde Martes')
    tarde_miercoles = models.BooleanField(default=False, verbose_name='Tarde Miércoles')
    tarde_jueves = models.BooleanField(default=False, verbose_name='Tarde Jueves')
    tarde_viernes = models.BooleanField(default=False, verbose_name='Tarde Viernes')
    tarde_sabado = models.BooleanField(default=False, verbose_name='Tarde Sábado')
    tarde_domingo = models.BooleanField(default=False, verbose_name='Tarde Domingo')

    mensaje_enviado = models.BooleanField(default=False)

    class Meta:
        ordering = ['nombre']
        verbose_name = 'Hermano'
        verbose_name_plural = 'Hermanos'

    def __str__(self):
        return self.nombre

    @property
    def manana_list(self):
        """Retorna la lista de días disponibles en la mañana"""
        dias = []
        if self.manana_lunes: dias.append('lunes')
        if self.manana_martes: dias.append('martes')
        if self.manana_miercoles: dias.append('miercoles')
        if self.manana_jueves: dias.append('jueves')
        if self.manana_viernes: dias.append('viernes')
        if self.manana_sabado: dias.append('sabado')
        if self.manana_domingo: dias.append('domingo')
        return dias

    @property
    def tarde_list(self):
        """Retorna la lista de días disponibles en la tarde"""
        dias = []
        if self.tarde_lunes: dias.append('lunes')
        if self.tarde_martes: dias.append('martes')
        if self.tarde_miercoles: dias.append('miercoles')
        if self.tarde_jueves: dias.append('jueves')
        if self.tarde_viernes: dias.append('viernes')
        if self.tarde_sabado: dias.append('sabado')
        if self.tarde_domingo: dias.append('domingo')
        return dias

    def set_mananas(self, dias_list):
        """Establece la disponibilidad de mañanas desde una lista de días"""
        self.manana_lunes = 'lunes' in dias_list
        self.manana_martes = 'martes' in dias_list
        self.manana_miercoles = 'miercoles' in dias_list
        self.manana_jueves = 'jueves' in dias_list
        self.manana_viernes = 'viernes' in dias_list
        self.manana_sabado = 'sabado' in dias_list
        self.manana_domingo = 'domingo' in dias_list

    def set_tardes(self, dias_list):
        """Establece la disponibilidad de tardes desde una lista de días"""
        self.tarde_lunes = 'lunes' in dias_list
        self.tarde_martes = 'martes' in dias_list
        self.tarde_miercoles = 'miercoles' in dias_list
        self.tarde_jueves = 'jueves' in dias_list
        self.tarde_viernes = 'viernes' in dias_list
        self.tarde_sabado = 'sabado' in dias_list
        self.tarde_domingo = 'domingo' in dias_list


class Casa(models.Model):
    """Modelo que representa una casa con su disponibilidad semanal"""

    nombre = models.CharField(max_length=200, unique=True)
    direccion = models.CharField(max_length=300, blank=True, default='')
    numero = models.CharField(max_length=20, blank=True, default='')
    comentario = models.TextField(blank=True, default='')

    # Disponibilidad Mañanas - cada día es un booleano
    manana_lunes = models.BooleanField(default=False, verbose_name='Mañana Lunes')
    manana_martes = models.BooleanField(default=False, verbose_name='Mañana Martes')
    manana_miercoles = models.BooleanField(default=False, verbose_name='Mañana Miércoles')
    manana_jueves = models.BooleanField(default=False, verbose_name='Mañana Jueves')
    manana_viernes = models.BooleanField(default=False, verbose_name='Mañana Viernes')
    manana_sabado = models.BooleanField(default=False, verbose_name='Mañana Sábado')
    manana_domingo = models.BooleanField(default=False, verbose_name='Mañana Domingo')

    # Disponibilidad Tardes
    tarde_lunes = models.BooleanField(default=False, verbose_name='Tarde Lunes')
    tarde_martes = models.BooleanField(default=False, verbose_name='Tarde Martes')
    tarde_miercoles = models.BooleanField(default=False, verbose_name='Tarde Miércoles')
    tarde_jueves = models.BooleanField(default=False, verbose_name='Tarde Jueves')
    tarde_viernes = models.BooleanField(default=False, verbose_name='Tarde Viernes')
    tarde_sabado = models.BooleanField(default=False, verbose_name='Tarde Sábado')
    tarde_domingo = models.BooleanField(default=False, verbose_name='Tarde Domingo')

    mensaje_enviado = models.BooleanField(default=False)

    # Disponibilidad Cartas Tardes
    cartas_tarde_lunes = models.BooleanField(default=False, verbose_name='Cartas Tarde Lunes')
    cartas_tarde_martes = models.BooleanField(default=False, verbose_name='Cartas Tarde Martes')
    cartas_tarde_miercoles = models.BooleanField(default=False, verbose_name='Cartas Tarde Miércoles')
    cartas_tarde_jueves = models.BooleanField(default=False, verbose_name='Cartas Tarde Jueves')
    cartas_tarde_viernes = models.BooleanField(default=False, verbose_name='Cartas Tarde Viernes')
    cartas_tarde_sabado = models.BooleanField(default=False, verbose_name='Cartas Tarde Sábado')
    cartas_tarde_domingo = models.BooleanField(default=False, verbose_name='Cartas Tarde Domingo')

    class Meta:
        ordering = ['nombre']
        verbose_name = 'Casa'
        verbose_name_plural = 'Casas'

    def __str__(self):
        return f"{self.nombre} - {self.direccion}"

    @property
    def manana_list(self):
        """Retorna la lista de días disponibles en la mañana"""
        dias = []
        if self.manana_lunes: dias.append('lunes')
        if self.manana_martes: dias.append('martes')
        if self.manana_miercoles: dias.append('miercoles')
        if self.manana_jueves: dias.append('jueves')
        if self.manana_viernes: dias.append('viernes')
        if self.manana_sabado: dias.append('sabado')
        if self.manana_domingo: dias.append('domingo')
        return dias

    @property
    def tarde_list(self):
        """Retorna la lista de días disponibles en la tarde"""
        dias = []
        if self.tarde_lunes: dias.append('lunes')
        if self.tarde_martes: dias.append('martes')
        if self.tarde_miercoles: dias.append('miercoles')
        if self.tarde_jueves: dias.append('jueves')
        if self.tarde_viernes: dias.append('viernes')
        if self.tarde_sabado: dias.append('sabado')
        if self.tarde_domingo: dias.append('domingo')
        return dias

    def set_mananas(self, dias_list):
        """Establece la disponibilidad de mañanas desde una lista de días"""
        self.manana_lunes = 'lunes' in dias_list
        self.manana_martes = 'martes' in dias_list
        self.manana_miercoles = 'miercoles' in dias_list
        self.manana_jueves = 'jueves' in dias_list
        self.manana_viernes = 'viernes' in dias_list
        self.manana_sabado = 'sabado' in dias_list
        self.manana_domingo = 'domingo' in dias_list

    def set_tardes(self, dias_list):
        """Establece la disponibilidad de tardes desde una lista de días"""
        self.tarde_lunes = 'lunes' in dias_list
        self.tarde_martes = 'martes' in dias_list
        self.tarde_miercoles = 'miercoles' in dias_list
        self.tarde_jueves = 'jueves' in dias_list
        self.tarde_viernes = 'viernes' in dias_list
        self.tarde_sabado = 'sabado' in dias_list
        self.tarde_domingo = 'domingo' in dias_list

    @property
    def cartas_tarde_list(self):
        """Retorna la lista de días disponibles para cartas en la tarde"""
        dias = []
        if self.cartas_tarde_lunes: dias.append('lunes')
        if self.cartas_tarde_martes: dias.append('martes')
        if self.cartas_tarde_miercoles: dias.append('miercoles')
        if self.cartas_tarde_jueves: dias.append('jueves')
        if self.cartas_tarde_viernes: dias.append('viernes')
        if self.cartas_tarde_sabado: dias.append('sabado')
        if self.cartas_tarde_domingo: dias.append('domingo')
        return dias

    def set_cartas_tarde(self, dias_list):
        """Establece la disponibilidad de cartas tarde desde una lista de días"""
        self.cartas_tarde_lunes = 'lunes' in dias_list
        self.cartas_tarde_martes = 'martes' in dias_list
        self.cartas_tarde_miercoles = 'miercoles' in dias_list
        self.cartas_tarde_jueves = 'jueves' in dias_list
        self.cartas_tarde_viernes = 'viernes' in dias_list
        self.cartas_tarde_sabado = 'sabado' in dias_list
        self.cartas_tarde_domingo = 'domingo' in dias_list
