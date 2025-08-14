from PySide6.QtWidgets import QPushButton, QFrame, QSizePolicy
from PySide6.QtGui import QColor, QPainter, QPainterPath, QPen, QFont, QPalette, QLinearGradient, QFontMetrics
from PySide6.QtCore import Qt, QRect, QPointF, QSize
import random

class FantasyButton(QPushButton):  # Fixed: Inherits from QPushButton
    def __init__(self, text, parent=None):
        super().__init__(text, parent)
        self.setMinimumHeight(40)
        self.setSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Fixed)
        self.setCursor(Qt.PointingHandCursor)
        self.font = QFont("Georgia", 12)
        self.font.setBold(True)
        
    def paintEvent(self, event):
        painter = QPainter(self)
        painter.setRenderHint(QPainter.Antialiasing)
        
        # Create parchment-like background
        bg_color = QColor(245, 235, 215)
        border_color = QColor(160, 130, 90)
        
        # Draw main button shape
        path = QPainterPath()
        path.addRoundedRect(1, 1, self.width()-2, self.height()-2, 8, 8)
        
        # Fill with parchment color
        painter.fillPath(path, bg_color)
        
        # Draw decorative border
        pen = QPen(border_color, 2)
        painter.setPen(pen)
        painter.drawPath(path)
        
        # Draw inner decorative line
        inner_path = QPainterPath()
        inner_path.addRoundedRect(4, 4, self.width()-8, self.height()-8, 6, 6)
        painter.setPen(QPen(border_color, 1))
        painter.drawPath(inner_path)
        
        # Draw text
        painter.setFont(self.font)
        painter.setPen(QColor(0, 0, 0))  # Black text
        painter.drawText(self.rect(), Qt.AlignCenter, self.text())

class WEndTabButton(QPushButton):
    def __init__(self, text, parent=None):
        super().__init__(text, parent)
        self.setMinimumHeight(40)
        self.setSizePolicy(QSizePolicy.Policy.MinimumExpanding, QSizePolicy.Policy.Fixed)
        self.setCursor(Qt.PointingHandCursor)
        self.font = QFont("Georgia", 11)
        self.font.setBold(True)
        
        # Calculate minimum width based on text
        metrics = QFontMetrics(self.font)
        self.text_width = metrics.horizontalAdvance(text) + 100  # Extra space for W shape
        self.setMinimumWidth(self.text_width)
        
    def sizeHint(self):
        return QSize(self.text_width, 40)
    
    def paintEvent(self, event):
        painter = QPainter(self)
        painter.setRenderHint(QPainter.Antialiasing)
        
        # Tab dimensions
        tab_width = self.width()
        tab_height = self.height()
        w_width = 40  # Width of the W shape section
        
        # Create W-shaped path as specified
        path = QPainterPath()
        path.moveTo(0, 0)  # Top-left
        path.lineTo(tab_width, 0)  # Top-right
        path.lineTo(tab_width - (w_width/2), tab_height/2)  # Valley point
        path.lineTo(tab_width, tab_height)  # Bottom-right
        path.lineTo(0, tab_height)  # Bottom-left
        path.closeSubpath()  # Close to top-left
        
        # Create gradient for tab effect
        gradient = QLinearGradient(0, 0, tab_width, 0)
        gradient.setColorAt(0, QColor(180, 150, 100))  # Darker at attachment
        gradient.setColorAt(0.7, QColor(210, 180, 130))  # Lighter at text area
        gradient.setColorAt(1, QColor(180, 150, 100))  # Darker at W shape
        
        # Fill tab shape
        painter.fillPath(path, gradient)
        
        # Draw decorative border
        painter.setPen(QPen(QColor(130, 100, 70), 2))
        painter.drawPath(path)
        
        # Draw stitching details
        painter.setPen(QPen(QColor(200, 180, 150), 1))
        
        # Vertical stitching lines only on the flat left part
        stitch_width = tab_width - w_width
        if stitch_width > 50:  # Only draw if there's enough space
            # Calculate spacing for 3-5 stitches based on button width
            num_stitches = min(5, max(3, int(stitch_width / 30)))
            for i in range(1, num_stitches + 1):
                x_pos = stitch_width * i / (num_stitches + 1)
                # Draw from top to bottom, but avoid the W shape area
                painter.drawLine(x_pos, 5, x_pos, tab_height - 5)
        
        # Draw W-shape stitching
        # Top horizontal line
        painter.drawLine(tab_width - w_width, 5, tab_width, 5)
        # Bottom horizontal line
        painter.drawLine(tab_width - w_width, tab_height - 5, tab_width, tab_height - 5)
        # Diagonal lines forming the W
        painter.drawLine(tab_width, 0, tab_width - (w_width/2), tab_height/2)
        painter.drawLine(tab_width - (w_width/2), tab_height/2, tab_width, tab_height)
        
        # Draw text
        painter.setFont(self.font)
        painter.setPen(QColor(50, 30, 10))  # Dark brown text
        
        # Position text in the middle section (avoiding W shape area)
        text_rect = QRect(10, 0, tab_width - w_width - 20, tab_height)
        painter.drawText(text_rect, Qt.AlignCenter, self.text())
        
        # Add hover effect
        if self.underMouse():
            highlight = QColor(255, 255, 255, 80)
            painter.fillPath(path, highlight)
            
        # Add shadow effect for depth
        shadow = QColor(0, 0, 0, 50)
        painter.setPen(Qt.NoPen)
        painter.setBrush(shadow)
        shadow_path = QPainterPath(path)
        shadow_path.translate(2, 2)
        painter.drawPath(shadow_path)


class BookPage(QFrame):
    def __init__(self, side="left", parent=None):
        super().__init__(parent)
        self.side = side
        self.setSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Expanding)
        
        # Set parchment background
        palette = self.palette()
        palette.setColor(QPalette.Window, QColor(250, 240, 220))
        self.setPalette(palette)
        self.setAutoFillBackground(True)
    
    def paintEvent(self, event):
        painter = QPainter(self)
        painter.setRenderHint(QPainter.Antialiasing)
        
        # Draw parchment texture
        for _ in range(200):
            x = random.randint(0, self.width())
            y = random.randint(0, self.height())
            w = random.randint(2, 8)
            h = random.randint(2, 8)
            alpha = random.randint(5, 15)
            color = QColor(220, 200, 170, alpha)
            painter.setPen(Qt.NoPen)
            painter.setBrush(color)
            painter.drawEllipse(x, y, w, h)
        
        # Draw border
        border_color = QColor(160, 130, 90)
        painter.setPen(QPen(border_color, 1))
        painter.drawRect(0, 0, self.width()-1, self.height()-1)
        
        # Draw inner margin
        margin = 15
        painter.setPen(QPen(border_color, 1, Qt.DashLine))
        painter.drawRect(margin, margin, self.width()-margin*2, self.height()-margin*2)
        
        # Draw binding effect
        if self.side == "left":
            # Right edge binding
            binding_rect = QRect(self.width()-2, 0, 2, self.height())
            painter.fillRect(binding_rect, QColor(100, 80, 60))
        else:
            # Left edge binding
            binding_rect = QRect(0, 0, 2, self.height())
            painter.fillRect(binding_rect, QColor(100, 80, 60))