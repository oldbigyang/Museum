import os
import json
from django.core.management.base import BaseCommand
from artifacts.models import Artifact

class Command(BaseCommand):
    help = 'Import artifacts from JSON files'

    def handle(self, *args, **kwargs):
        directory = '/home/hongdayang/tmp/'  # 替换为你的 JSON 文件目录
        error_files = []  # 用于记录出错的文件

        # 字段映射
        data_mapping = {
            "年": "year",
            "月": "month",
            "日": "day",
            "总登记号": "registration_number",
            "分类号": "classification_number",
            "名称": "name",
            "年代": "era",
            "件数": "quantity",
            "单位": "unit",
            "尺寸": "size",
            "重量": "weight",
            "质地": "texture",
            "完残情况": "condition",
            "来源": "source",
            "入馆凭证号": "entrance_certificate_number",
            "注销凭证号": "cancellation_certificate_number",
            "级别": "level",
            "备注": "remarks",
            "负责人": "person_in_charge",
            "档案编号": "file_number",
            "形状内容描述": "shape_description",
            "当前保存条件": "current_storage_conditions",
            "铭记题跋": "inscriptions", 
        }

        for filename in os.listdir(directory):
            if filename.endswith('.json'):
                file_path = os.path.join(directory, filename)
                
                # 检查文件是否为空
                if os.path.getsize(file_path) == 0:
                    self.stdout.write(self.style.ERROR(f'{filename} is empty'))
                    error_files.append(filename)
                    continue

                try:
                    with open(file_path, 'r', encoding='utf-8') as file:
                        json_data = json.load(file)

                        # 映射 JSON 数据到模型字段
                        data = {db_field: json_data[json_field] for json_field, db_field in data_mapping.items() if json_field in json_data}

                        # 保存到数据库
                        artifact = Artifact(**data)
                        artifact.save()
                        self.stdout.write(self.style.SUCCESS(f'Successfully imported {filename}'))

                except json.JSONDecodeError as e:
                    self.stdout.write(self.style.ERROR(f'JSONDecodeError in {filename}: {e}'))
                    error_files.append(filename)
                except Exception as e:
                    self.stdout.write(self.style.ERROR(f'Error importing {filename}: {e}'))
                    error_files.append(filename)

        # 输出所有错误文件
        if error_files:
            self.stdout.write(self.style.ERROR('The following files encountered errors:'))
            for error_file in error_files:
                self.stdout.write(self.style.ERROR(f' - {error_file}'))
        else:
            self.stdout.write(self.style.SUCCESS('All files processed successfully!'))

