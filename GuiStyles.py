# Subject: ITU
# School:  Faculty of Information Technology, Brno University of Technology
# Authors: Boris Burkalo
#          Daniel Kamenický
#          Jan Klusáček
#
class Style():
    buttonToggle = (
    """
    QPushButton {
	border: none;
	background-color: rgb(27, 29, 35);
    }
    QPushButton:hover {
    	background-color: rgb(20, 29, 35);
    }
    """
    )

    buttonStandard = (
    """
    QPushButton {
	border: none;
	background-color: rgb(27, 29, 35);
    text-align: left;
    font-size: 15px;
    font-weight: bold;
    padding-left: 22px;
    color: rgb(255, 255, 255);
    }
    QPushButton:hover {
    	background-color: rgb(20, 29, 35);
    }
    QPushButton:pressed {
    	background-color: rgba(85, 170, 255, 100);
    }
    """
    )

    buttonClicked = (
    """
    QPushButton {
    	border: none;
    	background-color: rgb(115, 210, 22);
        text-align: left;
        font-size: 15px;
        font-weight: bold;
        padding-left: 22px;
        color: rgb(0, 0, 0);
    }
    """
    )

    lineEditWrong = (
    """
    QLineEdit {
	background-color: rgb(27, 29, 35);
	border-radius: 5px;
	border: 2px solid rgb(164, 0, 0);
	padding-left: 10px;
    }
    QLineEdit:hover {
	border: 2px solid rgb(64, 71, 88);
    }
    QLineEdit:focus {
	border: 2px solid rgb(91, 101, 124);
    }
    """
    )

    lineEdit = (
    """
    QLineEdit {
	background-color: rgb(27, 29, 35);
	border-radius: 5px;
	border: 2px solid rgb(27, 29, 35);
	padding-left: 10px;
    }
    QLineEdit:hover {
	border: 2px solid rgb(64, 71, 88);
    }
    QLineEdit:focus {
	border: 2px solid rgb(91, 101, 124);
    }
    """
    )

    messageBoxButton = (
    """
    QPushButton {
	background-color: rgba(115, 210, 22, 150);
	color: rgb(0, 0, 0);
	border: 0px solid rgba(115, 210, 22, 150);
	border-radius: 5px;
    min-width: 75px;
    min-height: 20px;
    padding-left:20px;
    padding-right:20px;
    }
    QPushButton:hover {
	background-color: rgba(115, 210, 22, 200);
    }
    QPushButton:pressed {
	background-color: rgba(85, 170, 255, 100);
    }
    """
    )

    messageBox = (
    """
    QMessageBox {
	background-color: rgb(27, 29, 35);
    color: rgb(255, 255, 255);
    }
    QLabel {
    color: rgb(255, 255, 255);
    qproperty-alignment: AlignCenter;
    }
    """
    )
