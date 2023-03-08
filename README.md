

# Pytest CI CD

### Türkçe
Bu GitHub deposu, GitHub Actions ve pytest kullanarak basit bir proje yapmak için oluşturulmuştur.

## Kurulum

Bu projeyi çalıştırmak için şunları yapmanız gerekir:

1.  Bu depoyu kopyalayın: `git clone https://github.com/MrSipahi/pytest-CI-CD.git`
2.  Proje dizinine gidin: `cd pytest-CI-CD`
3.  Gerekli bağımlılıkları yükleyin: `pip install -r requirements.txt`

## Kullanım

Bu projeyi kullanmak için aşağıdaki adımları izleyebilirsiniz:

1.  Testleri çalıştırmak için aşağıdaki komutu çalıştırın: `pytest`
2.  Test sonuçlarını görüntülemek için `coverage` raporunu oluşturun: `coverage run -m pytest `
3.  `coverage` raporunu görüntülemek için aşağıdaki komutu çalıştırın: `coverage report -m`
4.  `flake8` stil doğrulaması yapmak için aşağıdaki komutu çalıştırın: `flake8`

## GitHub Actions

Bu proje, GitHub Actions kullanarak testleri ve stil doğrulamasını otomatik olarak çalıştırmak için yapılandırılmıştır. Herhangi bir değişiklik yaptığınızda, GitHub Actions otomatik olarak çalışacak ve herhangi bir hata varsa size bildirecektir.

## Katkıda Bulunma

Bu projeye katkıda bulunmak isterseniz, lütfen bir çekme isteği gönderin. Kabul edilebilir bir değişiklik önerdiğinizde, birlikte projeyi güncelleyebiliriz.



### English
This GitHub repository is created to build a simple project using GitHub Actions and pytest.

## Installation

To run this project, you need to:

1.  Clone this repository: `git clone https://github.com/MrSipahi/pytest-CI-CD.git`
2.  Go to the project directory: `cd pytest-CI-CD`
3.  Install the required dependencies: `pip install -r requirements.txt`

## Usage

You can use this project by following these steps:

1.  Run the tests by executing the following command: `pytest`
2.  Generate a `coverage` report to view the test results: `coverage run -m pytest`
3.  View the `coverage` report by executing the following command: `coverage report -m`
4.  Perform style validation with `flake8` by running the following command: `flake8`

## GitHub Actions

This project is configured to run tests and style validation automatically using GitHub Actions. Whenever you make any changes, GitHub Actions will automatically run and notify you if there are any errors.

## Contribution

If you want to contribute to this project, please submit a pull request. When you propose an acceptable change, we can work together to update the project.