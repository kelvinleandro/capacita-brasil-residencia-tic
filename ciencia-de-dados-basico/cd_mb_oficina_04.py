import numpy as np
import pandas as pd

nums = np.array([12, 45, 67, 23, 89, 34, 22, 90, 56, 78])
media = np.mean(nums)
maiores_media = nums[nums > media]
maiores_media_df = pd.DataFrame(maiores_media, columns=["maiores_que_media"])

print(f"Media = {media}")
print(maiores_media_df)

maiores_media_df.to_csv("maiores_que_media.csv", index=False)
