import sys
from PyQt5.QtWidgets import (
    QApplication, QMainWindow, QVBoxLayout, QHBoxLayout, QWidget,
    QLabel, QSlider, QPushButton, QLineEdit, QGridLayout
)
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QPainter, QColor
import matplotlib.pyplot as plt
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas

# Константы
TARGET_GLUCOSE = 5.5  # Целевой уровень глюкозы
GLUCOSE_RANGE = (4.0, 7.0)  # Диапазон нормы
TIME_STEP = 1  # Шаг времени в часах

class RubiksCube(QWidget):
    """Виджет для визуализации кубика Рубика."""
    def __init__(self, is_solved=True):
        super().__init__()
        self.is_solved = is_solved

    def paintEvent(self, event):
        painter = QPainter(self)
        size = min(self.width(), self.height())
        cube_size = size // 3

        for i in range(3):
            for j in range(3):
                x = i * cube_size
                y = j * cube_size
                if self.is_solved:
                    color = QColor(0, 255, 0)  # Зеленый (собран)
                else:
                    color = QColor(255, 0, 0)  # Красный (сломан)
                painter.fillRect(x, y, cube_size, cube_size, color)

class DiabetesSimulator(QMainWindow):
    """Основное окно приложения."""
    def __init__(self):
        super().__init__()
        self.glucose_level = TARGET_GLUCOSE  # Начальный уровень глюкозы
        self.time = 0  # Время в часах
        self.glucose_history = [TARGET_GLUCOSE]  # История уровней глюкозы
        self.time_history = [0]  # Временные метки
        self.init_ui()

    def init_ui(self):
        self.setWindowTitle("Тренажер по сахарному диабету")
        self.setGeometry(100, 100, 1000, 600)

        # Главный контейнер
        central_widget = QWidget()
        self.setCentralWidget(central_widget)
        layout = QHBoxLayout()

        # Левая панель: управление параметрами
        control_panel = QVBoxLayout()

        # Инсулин
        insulin_label = QLabel("Доза инсулина (Ед.):")
        self.insulin_input = QLineEdit("10")
        control_panel.addWidget(insulin_label)
        control_panel.addWidget(self.insulin_input)

        # Углеводы
        carbs_label = QLabel("Углеводы (г):")
        self.carbs_input = QLineEdit("60")
        control_panel.addWidget(carbs_label)
        control_panel.addWidget(self.carbs_input)

        # Гликемическая нагрузка (ГН)
        glycemic_load_label = QLabel("Гликемическая нагрузка (ГН):")
        self.glycemic_load_input = QLineEdit("20")
        control_panel.addWidget(glycemic_load_label)
        control_panel.addWidget(self.glycemic_load_input)

        # Активность
        activity_label = QLabel("Физическая активность (мин):")
        self.activity_slider = QSlider(Qt.Horizontal)
        self.activity_slider.setMinimum(0)
        self.activity_slider.setMaximum(120)
        self.activity_slider.setValue(30)
        control_panel.addWidget(activity_label)
        control_panel.addWidget(self.activity_slider)

        # Кнопка "Применить"
        apply_button = QPushButton("Применить изменения")
        apply_button.clicked.connect(self.apply_changes)
        control_panel.addWidget(apply_button)

        # Кнопка "Сбросить"
        reset_button = QPushButton("Сбросить")
        reset_button.clicked.connect(self.reset_state)
        control_panel.addWidget(reset_button)

        # Правая панель: визуализация
        visualization_panel = QVBoxLayout()

        # Кубик Рубика
        self.cube = RubiksCube(is_solved=True)
        visualization_panel.addWidget(self.cube)

        # Уровень глюкозы
        self.glucose_label = QLabel(f"Уровень глюкозы: {self.glucose_level:.1f} ммоль/л")
        visualization_panel.addWidget(self.glucose_label)

        # График
        self.figure, self.ax = plt.subplots()
        self.canvas = FigureCanvas(self.figure)
        visualization_panel.addWidget(self.canvas)

        # Объединяем панели
        layout.addLayout(control_panel)
        layout.addLayout(visualization_panel)
        central_widget.setLayout(layout)

    def apply_changes(self):
        """Применить изменения параметров и пересчитать уровень глюкозы."""
        try:
            insulin = float(self.insulin_input.text())
            carbs = float(self.carbs_input.text())
            glycemic_load = float(self.glycemic_load_input.text())
            activity = self.activity_slider.value()

            # Улучшенная модель расчета уровня глюкозы
            glucose_change = (
                (carbs / 10) * (glycemic_load / 20)  # Учет ГН
                - (insulin * 0.5)  # Влияние инсулина
                + (activity / 60)  # Влияние активности
            )
            self.glucose_level += glucose_change

            # Обновляем историю
            self.time += TIME_STEP
            self.glucose_history.append(self.glucose_level)
            self.time_history.append(self.time)

            # Обновляем интерфейс
            self.glucose_label.setText(f"Уровень глюкозы: {self.glucose_level:.1f} ммоль/л")
            self.cube.is_solved = GLUCOSE_RANGE[0] <= self.glucose_level <= GLUCOSE_RANGE[1]
            self.cube.update()

            # Обновляем график
            self.update_graph()
        except ValueError:
            self.glucose_label.setText("Ошибка ввода!")

    def update_graph(self):
        """Обновить график изменения уровня глюкозы."""
        self.ax.clear()
        self.ax.plot(self.time_history, self.glucose_history, marker='o', label="Уровень глюкозы")
        self.ax.axhline(TARGET_GLUCOSE, color='green', linestyle='--', label="Целевой уровень")
        self.ax.fill_between(
            self.time_history,
            GLUCOSE_RANGE[0],
            GLUCOSE_RANGE[1],
            color='lightgreen',
            alpha=0.3,
            label="Норма"
        )
        self.ax.set_xlabel("Время (часы)")
        self.ax.set_ylabel("Уровень глюкозы (ммоль/л)")
        self.ax.legend()
        self.canvas.draw()

    def reset_state(self):
        """Сбросить состояние к начальному."""
        self.glucose_level = TARGET_GLUCOSE
        self.time = 0
        self.glucose_history = [TARGET_GLUCOSE]
        self.time_history = [0]

        self.insulin_input.setText("10")
        self.carbs_input.setText("60")
        self.glycemic_load_input.setText("20")
        self.activity_slider.setValue(30)

        self.glucose_label.setText(f"Уровень глюкозы: {self.glucose_level:.1f} ммоль/л")
        self.cube.is_solved = True
        self.cube.update()

        self.update_graph()

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = DiabetesSimulator()
    window.show()
    sys.exit(app.exec_())