"""
Chart Generation Script
Employee Attrition and Workforce Analysis
IBM SkillsBuild Data Analytics with AI Academic Internship Program
Student: Anish Kumar

Run this script to generate all chart PNG files used by the notebook and report.
Usage: python generate_charts.py
"""

import pandas as pd
import numpy as np
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
import seaborn as sns
import os
import warnings
warnings.filterwarnings('ignore')

# ── Style Configuration ──────────────────────────────────────────────────────
plt.rcParams.update({
    'figure.dpi': 150,
    'font.family': 'DejaVu Sans',
    'font.size': 11,
    'axes.spines.top': False,
    'axes.spines.right': False,
    'axes.grid': True,
    'axes.grid.axis': 'y',
    'grid.alpha': 0.3,
    'grid.linestyle': '--',
})
sns.set_style('whitegrid')

PALETTE_MAIN   = ['#2563eb', '#dc2626', '#16a34a', '#d97706', '#7c3aed', '#0891b2', '#be123c', '#15803d', '#c2410c']
COLOR_YES      = '#dc2626'
COLOR_NO       = '#2563eb'
COLOR_ACCENT   = '#2563eb'
AVG_LINE_COLOR = '#64748b'
AVG_LINE_RATE  = 16.12

OUTPUT_DIR = os.path.dirname(os.path.abspath(__file__))

# ── Load & Prepare Data ───────────────────────────────────────────────────────
df = pd.read_csv(os.path.join(OUTPUT_DIR, 'WA_Fn-UseC_-HR-Employee-Attrition.csv'))
df_clean = df.drop(columns=['EmployeeCount', 'StandardHours', 'Over18', 'EmployeeNumber'])
df_clean['AgeGroup']   = pd.cut(df_clean['Age'],            bins=[18,25,35,45,55,65],    labels=['18-25','26-35','36-45','46-55','56-65'])
df_clean['TenureGroup']= pd.cut(df_clean['YearsAtCompany'], bins=[-1,2,5,10,20,100],     labels=['0-2 yrs','3-5 yrs','6-10 yrs','11-20 yrs','20+ yrs'])
df_clean['IncomeGroup']= pd.cut(df_clean['MonthlyIncome'],  bins=[0,3000,6000,10000,20000],labels=['Low (<3K)','Mid (3K-6K)','High (6K-10K)','Very High (>10K)'])
df_clean['AttritionBinary'] = (df_clean['Attrition'] == 'Yes').astype(int)

def attrition_summary(df, col):
    r = df.groupby(col, observed=True).agg(
        Total=('Attrition','count'),
        Left=('Attrition', lambda x: (x=='Yes').sum())
    ).reset_index()
    r['Rate'] = (r['Left'] / r['Total'] * 100).round(2)
    return r

def add_bar_labels(ax, bars, fmt='{:.1f}%', offset=0.4, color='#1e293b'):
    for bar in bars:
        h = bar.get_height()
        ax.text(bar.get_x() + bar.get_width()/2, h + offset,
                fmt.format(h), ha='center', va='bottom',
                fontsize=9, fontweight='bold', color=color)

def add_hbar_labels(ax, bars, fmt='${:,.0f}', offset=100, color='#1e293b'):
    for bar in bars:
        w = bar.get_width()
        ax.text(w + offset, bar.get_y() + bar.get_height()/2,
                fmt.format(w), ha='left', va='center',
                fontsize=9, fontweight='bold', color=color)

def save(name):
    path = os.path.join(OUTPUT_DIR, name)
    plt.savefig(path, dpi=150, bbox_inches='tight', facecolor='white')
    plt.close()
    print(f'  Saved: {name}')

print('Generating charts...')

# ── Chart 1: KPI Summary Dashboard ───────────────────────────────────────────
print('Chart 1: KPI Dashboard')
fig, axes = plt.subplots(2, 4, figsize=(16, 6))
fig.patch.set_facecolor('#0f172a')
metrics = [
    ('1,470', 'Total\nEmployees',    '#2563eb'),
    ('237',   'Employees\nWho Left', '#dc2626'),
    ('1,233', 'Active\nEmployees',   '#16a34a'),
    ('16.12%','Attrition\nRate',     '#d97706'),
    ('$6,503','Avg Monthly\nIncome', '#7c3aed'),
    ('36.92', 'Average\nAge',        '#0891b2'),
    ('2.73/4','Avg Job\nSatisfaction','#be123c'),
    ('7.01',  'Avg Years at\nCompany','#15803d'),
]
for ax, (val, label, color) in zip(axes.flat, metrics):
    ax.set_facecolor('#1e293b')
    for sp in ax.spines.values(): sp.set_visible(False)
    ax.set_xticks([]); ax.set_yticks([])
    ax.text(0.5, 0.60, val,   transform=ax.transAxes, ha='center', va='center',
            fontsize=22, fontweight='bold', color=color)
    ax.text(0.5, 0.22, label, transform=ax.transAxes, ha='center', va='center',
            fontsize=10, color='#94a3b8')
fig.suptitle('Employee Attrition — Key Performance Indicators',
             fontsize=14, fontweight='bold', color='white', y=1.01)
plt.tight_layout(pad=1.2)
save('chart_00_kpi_dashboard.png')

# ── Chart 2: Attrition Overview Donut ────────────────────────────────────────
print('Chart 2: Attrition Overview Donut')
fig, ax = plt.subplots(figsize=(7, 6))
sizes = [1233, 237]
labels = ['Active (83.88%)', 'Left (16.12%)']
colors = [COLOR_NO, COLOR_YES]
wedges, texts, autotexts = ax.pie(
    sizes, labels=labels, colors=colors, autopct='%1.1f%%',
    startangle=90, pctdistance=0.78,
    wedgeprops={'width': 0.55, 'edgecolor': 'white', 'linewidth': 2}
)
for at in autotexts:
    at.set_fontsize(12); at.set_fontweight('bold'); at.set_color('white')
for t in texts:
    t.set_fontsize(11)
ax.text(0, 0, '1,470\nEmployees', ha='center', va='center',
        fontsize=13, fontweight='bold', color='#1e293b')
ax.set_title('Overall Employee Attrition', fontsize=14, fontweight='bold', pad=16)
plt.tight_layout()
save('chart_01_attrition_overview.png')

# ── Chart 3: Attrition by Department ─────────────────────────────────────────
print('Chart 3: Attrition by Department')
dept = attrition_summary(df_clean, 'Department')
fig, ax = plt.subplots(figsize=(9, 5))
colors_d = [COLOR_YES if v > AVG_LINE_RATE else COLOR_NO for v in dept['Rate']]
bars = ax.bar(dept['Department'], dept['Rate'], color=colors_d, edgecolor='white', width=0.5, zorder=3)
add_bar_labels(ax, bars)
ax.axhline(AVG_LINE_RATE, color=AVG_LINE_COLOR, linestyle='--', linewidth=1.5, zorder=2,
           label=f'Company Avg ({AVG_LINE_RATE}%)')
ax.set_title('Attrition Rate by Department', fontsize=14, fontweight='bold', pad=12)
ax.set_xlabel('Department', fontsize=11); ax.set_ylabel('Attrition Rate (%)', fontsize=11)
ax.set_ylim(0, 30); ax.legend(fontsize=9)
red_p  = mpatches.Patch(color=COLOR_YES, label='Above average')
blue_p = mpatches.Patch(color=COLOR_NO,  label='Below average')
ax.legend(handles=[red_p, blue_p, plt.Line2D([0],[0],color=AVG_LINE_COLOR,linestyle='--',linewidth=1.5,label=f'Avg {AVG_LINE_RATE}%')],
          fontsize=9, framealpha=0.9)
plt.tight_layout()
save('chart_02_attrition_department.png')

# ── Chart 4: Attrition by Job Role (horizontal) ──────────────────────────────
print('Chart 4: Attrition by Job Role')
role = attrition_summary(df_clean, 'JobRole').sort_values('Rate', ascending=True)
fig, ax = plt.subplots(figsize=(11, 6))
colors_r = [COLOR_YES if v > AVG_LINE_RATE else COLOR_NO for v in role['Rate']]
bars = ax.barh(role['JobRole'], role['Rate'], color=colors_r, edgecolor='white', height=0.6, zorder=3)
for bar, val in zip(bars, role['Rate']):
    ax.text(bar.get_width() + 0.5, bar.get_y() + bar.get_height()/2,
            f'{val:.1f}%', va='center', fontsize=9, fontweight='bold', color='#1e293b')
ax.axvline(AVG_LINE_RATE, color=AVG_LINE_COLOR, linestyle='--', linewidth=1.5, zorder=2,
           label=f'Avg {AVG_LINE_RATE}%')
ax.set_title('Attrition Rate by Job Role', fontsize=14, fontweight='bold', pad=12)
ax.set_xlabel('Attrition Rate (%)', fontsize=11); ax.set_ylabel('Job Role', fontsize=11)
ax.set_xlim(0, 50); ax.legend(fontsize=9)
plt.tight_layout()
save('chart_03_attrition_jobrole.png')

# ── Chart 5: Overtime vs No Overtime ─────────────────────────────────────────
print('Chart 5: Overtime')
ot = attrition_summary(df_clean, 'OverTime')
fig, axes = plt.subplots(1, 2, figsize=(12, 5))
# Bar
colors_ot = [COLOR_NO, COLOR_YES]
bars = axes[0].bar(ot['OverTime'], ot['Rate'], color=colors_ot, edgecolor='white', width=0.45, zorder=3)
add_bar_labels(axes[0], bars, offset=0.8)
axes[0].axhline(AVG_LINE_RATE, color=AVG_LINE_COLOR, linestyle='--', linewidth=1.5, label=f'Avg {AVG_LINE_RATE}%')
axes[0].set_title('Attrition Rate by Overtime Status', fontsize=13, fontweight='bold')
axes[0].set_xlabel('Works Overtime', fontsize=11); axes[0].set_ylabel('Attrition Rate (%)', fontsize=11)
axes[0].set_ylim(0, 42); axes[0].legend(fontsize=9)
# Employee count comparison
ot_counts = df_clean.groupby(['OverTime', 'Attrition'], observed=True).size().unstack(fill_value=0)
ot_counts.plot(kind='bar', ax=axes[1], color=[COLOR_NO, COLOR_YES], edgecolor='white', rot=0)
axes[1].set_title('Employee Count: Overtime vs Attrition', fontsize=13, fontweight='bold')
axes[1].set_xlabel('Works Overtime', fontsize=11); axes[1].set_ylabel('Number of Employees', fontsize=11)
axes[1].legend(['Stayed', 'Left'], fontsize=9)
for container in axes[1].containers:
    axes[1].bar_label(container, fontsize=9, fontweight='bold')
plt.tight_layout()
save('chart_04_overtime.png')

# ── Chart 6: Age Group Attrition ─────────────────────────────────────────────
print('Chart 6: Age Group')
ag = attrition_summary(df_clean, 'AgeGroup')
palette_age = ['#dc2626','#ea580c','#ca8a04','#16a34a','#2563eb']
fig, ax = plt.subplots(figsize=(10, 5))
bars = ax.bar(ag['AgeGroup'].astype(str), ag['Rate'], color=palette_age, edgecolor='white', width=0.55, zorder=3)
add_bar_labels(ax, bars)
ax.axhline(AVG_LINE_RATE, color=AVG_LINE_COLOR, linestyle='--', linewidth=1.5, label=f'Avg {AVG_LINE_RATE}%')
ax.set_title('Attrition Rate by Age Group', fontsize=14, fontweight='bold', pad=12)
ax.set_xlabel('Age Group', fontsize=11); ax.set_ylabel('Attrition Rate (%)', fontsize=11)
ax.set_ylim(0, 45); ax.legend(fontsize=9)
# Add employee count annotations below bars
for bar, total in zip(bars, ag['Total']):
    ax.text(bar.get_x() + bar.get_width()/2, -2.5, f'n={total}',
            ha='center', fontsize=8, color='#64748b')
ax.set_ylim(-4, 45)
plt.tight_layout()
save('chart_05_age_group.png')

# ── Chart 7: Business Travel ──────────────────────────────────────────────────
print('Chart 7: Business Travel')
bt = attrition_summary(df_clean, 'BusinessTravel').sort_values('Rate', ascending=False)
fig, ax = plt.subplots(figsize=(9, 5))
colors_bt = [COLOR_YES, '#d97706', COLOR_NO]
bars = ax.bar(bt['BusinessTravel'], bt['Rate'], color=colors_bt, edgecolor='white', width=0.5, zorder=3)
add_bar_labels(ax, bars)
ax.axhline(AVG_LINE_RATE, color=AVG_LINE_COLOR, linestyle='--', linewidth=1.5, label=f'Avg {AVG_LINE_RATE}%')
ax.set_title('Attrition Rate by Business Travel Frequency', fontsize=14, fontweight='bold', pad=12)
ax.set_xlabel('Business Travel Category', fontsize=11); ax.set_ylabel('Attrition Rate (%)', fontsize=11)
ax.set_ylim(0, 35); ax.legend(fontsize=9)
plt.tight_layout()
save('chart_06_business_travel.png')

# ── Chart 8: Gender ───────────────────────────────────────────────────────────
print('Chart 8: Gender')
g = attrition_summary(df_clean, 'Gender')
fig, axes = plt.subplots(1, 2, figsize=(11, 5))
colors_g = ['#ec4899', '#3b82f6']
bars = axes[0].bar(g['Gender'], g['Rate'], color=colors_g, edgecolor='white', width=0.4, zorder=3)
add_bar_labels(axes[0], bars)
axes[0].axhline(AVG_LINE_RATE, color=AVG_LINE_COLOR, linestyle='--', linewidth=1.5, label=f'Avg {AVG_LINE_RATE}%')
axes[0].set_title('Attrition Rate by Gender', fontsize=13, fontweight='bold')
axes[0].set_ylabel('Attrition Rate (%)', fontsize=11); axes[0].set_ylim(0, 25); axes[0].legend(fontsize=9)
axes[1].pie(g['Left'], labels=g['Gender'], autopct='%1.1f%%', colors=colors_g,
            startangle=90, wedgeprops={'edgecolor':'white','linewidth':2})
axes[1].set_title('Share of Attrition by Gender', fontsize=13, fontweight='bold')
plt.tight_layout()
save('chart_07_gender.png')

# ── Chart 9: Marital Status ───────────────────────────────────────────────────
print('Chart 9: Marital Status')
ms = attrition_summary(df_clean, 'MaritalStatus').sort_values('Rate', ascending=False)
fig, ax = plt.subplots(figsize=(8, 5))
colors_ms = [COLOR_YES, COLOR_NO, '#16a34a']
bars = ax.bar(ms['MaritalStatus'], ms['Rate'], color=colors_ms, edgecolor='white', width=0.5, zorder=3)
add_bar_labels(ax, bars)
ax.axhline(AVG_LINE_RATE, color=AVG_LINE_COLOR, linestyle='--', linewidth=1.5, label=f'Avg {AVG_LINE_RATE}%')
ax.set_title('Attrition Rate by Marital Status', fontsize=14, fontweight='bold', pad=12)
ax.set_xlabel('Marital Status', fontsize=11); ax.set_ylabel('Attrition Rate (%)', fontsize=11)
ax.set_ylim(0, 35); ax.legend(fontsize=9)
plt.tight_layout()
save('chart_08_marital_status.png')

# ── Chart 10: Job Level ───────────────────────────────────────────────────────
print('Chart 10: Job Level')
jl = attrition_summary(df_clean, 'JobLevel')
colors_jl = ['#dc2626','#ea580c','#ca8a04','#16a34a','#2563eb']
fig, ax = plt.subplots(figsize=(9, 5))
bars = ax.bar(jl['JobLevel'].astype(str), jl['Rate'], color=colors_jl, edgecolor='white', width=0.55, zorder=3)
add_bar_labels(ax, bars)
ax.axhline(AVG_LINE_RATE, color=AVG_LINE_COLOR, linestyle='--', linewidth=1.5, label=f'Avg {AVG_LINE_RATE}%')
ax.set_title('Attrition Rate by Job Level', fontsize=14, fontweight='bold', pad=12)
ax.set_xlabel('Job Level  (1 = Entry  →  5 = Senior)', fontsize=11)
ax.set_ylabel('Attrition Rate (%)', fontsize=11)
ax.set_ylim(0, 35); ax.legend(fontsize=9)
plt.tight_layout()
save('chart_09_job_level.png')

# ── Chart 11: Job Satisfaction ────────────────────────────────────────────────
print('Chart 11: Job Satisfaction')
js = attrition_summary(df_clean, 'JobSatisfaction')
fig, ax = plt.subplots(figsize=(9, 5))
cmap_js = ['#dc2626','#ea580c','#2563eb','#16a34a']
bars = ax.bar(js['JobSatisfaction'].astype(str), js['Rate'], color=cmap_js, edgecolor='white', width=0.55, zorder=3)
add_bar_labels(ax, bars)
ax.axhline(AVG_LINE_RATE, color=AVG_LINE_COLOR, linestyle='--', linewidth=1.5, label=f'Avg {AVG_LINE_RATE}%')
ax.set_title('Attrition Rate by Job Satisfaction Level', fontsize=14, fontweight='bold', pad=12)
ax.set_xlabel('Job Satisfaction  (1=Low → 4=High)', fontsize=11)
ax.set_ylabel('Attrition Rate (%)', fontsize=11)
ax.set_ylim(0, 32); ax.legend(fontsize=9)
plt.tight_layout()
save('chart_10_job_satisfaction.png')

# ── Chart 12: Work-Life Balance ───────────────────────────────────────────────
print('Chart 12: Work-Life Balance')
wlb = attrition_summary(df_clean, 'WorkLifeBalance')
fig, ax = plt.subplots(figsize=(9, 5))
cmap_wlb = ['#dc2626','#ea580c','#2563eb','#16a34a']
bars = ax.bar(wlb['WorkLifeBalance'].astype(str), wlb['Rate'], color=cmap_wlb, edgecolor='white', width=0.55, zorder=3)
add_bar_labels(ax, bars)
ax.axhline(AVG_LINE_RATE, color=AVG_LINE_COLOR, linestyle='--', linewidth=1.5, label=f'Avg {AVG_LINE_RATE}%')
ax.set_title('Attrition Rate by Work-Life Balance Rating', fontsize=14, fontweight='bold', pad=12)
ax.set_xlabel('Work-Life Balance  (1=Bad → 4=Best)', fontsize=11)
ax.set_ylabel('Attrition Rate (%)', fontsize=11)
ax.set_ylim(0, 42); ax.legend(fontsize=9)
plt.tight_layout()
save('chart_11_work_life_balance.png')

# ── Chart 13: Monthly Income by Department & Role ─────────────────────────────
print('Chart 13: Income by Department & Role')
inc_dept = df_clean.groupby('Department')['MonthlyIncome'].mean().round(0).sort_values(ascending=True)
inc_role = df_clean.groupby('JobRole')['MonthlyIncome'].mean().round(0).sort_values(ascending=True)
fig, axes = plt.subplots(1, 2, figsize=(16, 5))
# Dept
colors_id = plt.cm.Blues(np.linspace(0.45, 0.85, len(inc_dept)))
bars = axes[0].barh(inc_dept.index, inc_dept.values, color=colors_id, edgecolor='white', height=0.45)
add_hbar_labels(axes[0], bars, fmt='${:,.0f}', offset=120)
axes[0].set_title('Avg Monthly Income by Department', fontsize=13, fontweight='bold')
axes[0].set_xlabel('Average Monthly Income ($)', fontsize=11); axes[0].set_xlim(0, 10500)
# Role
colors_ir = plt.cm.Blues(np.linspace(0.3, 0.9, len(inc_role)))
bars2 = axes[1].barh(inc_role.index, inc_role.values, color=colors_ir, edgecolor='white', height=0.6)
add_hbar_labels(axes[1], bars2, fmt='${:,.0f}', offset=150)
axes[1].set_title('Avg Monthly Income by Job Role', fontsize=13, fontweight='bold')
axes[1].set_xlabel('Average Monthly Income ($)', fontsize=11); axes[1].set_xlim(0, 21000)
plt.tight_layout()
save('chart_12_income.png')

# ── Chart 14: Tenure distribution + attrition overlay ────────────────────────
print('Chart 14: Years at Company Distribution')
fig, axes = plt.subplots(1, 2, figsize=(14, 5))
stayed = df_clean[df_clean['Attrition']=='No']['YearsAtCompany']
left   = df_clean[df_clean['Attrition']=='Yes']['YearsAtCompany']
bins_yr = np.arange(0, 41, 2)
axes[0].hist(stayed, bins=bins_yr, color=COLOR_NO, alpha=0.7, edgecolor='white', label='Stayed')
axes[0].hist(left,   bins=bins_yr, color=COLOR_YES, alpha=0.7, edgecolor='white', label='Left')
axes[0].axvline(stayed.mean(), color=COLOR_NO,  linestyle='--', linewidth=1.5, label=f'Stayed mean ({stayed.mean():.1f}yr)')
axes[0].axvline(left.mean(),   color=COLOR_YES, linestyle='--', linewidth=1.5, label=f'Left mean ({left.mean():.1f}yr)')
axes[0].set_title('Years at Company — Stayed vs Left', fontsize=13, fontweight='bold')
axes[0].set_xlabel('Years at Company', fontsize=11); axes[0].set_ylabel('Number of Employees', fontsize=11)
axes[0].legend(fontsize=9)
axes[1].hist(df_clean['MonthlyIncome'], bins=30, color='#7c3aed', edgecolor='white', alpha=0.85)
axes[1].axvline(df_clean['MonthlyIncome'].mean(),   color=COLOR_YES, linestyle='--', linewidth=1.5, label=f"Mean ${df_clean['MonthlyIncome'].mean():,.0f}")
axes[1].axvline(df_clean['MonthlyIncome'].median(), color=COLOR_NO,  linestyle='--', linewidth=1.5, label=f"Median ${df_clean['MonthlyIncome'].median():,.0f}")
axes[1].set_title('Monthly Income Distribution', fontsize=13, fontweight='bold')
axes[1].set_xlabel('Monthly Income ($)', fontsize=11); axes[1].set_ylabel('Number of Employees', fontsize=11)
axes[1].legend(fontsize=9)
plt.tight_layout()
save('chart_13_distributions.png')

# ── Chart 15: Stayed vs Left — Attribute Comparison ──────────────────────────
print('Chart 15: Stayed vs Left Comparison')
comp = df_clean.groupby('Attrition')[['Age','MonthlyIncome','YearsAtCompany','TotalWorkingYears']].mean().round(1)
attrs  = ['Age (yrs)', 'Monthly Income ($)', 'Years at Company', 'Total Working Years']
stayed_vals = comp.loc['No'].values
left_vals   = comp.loc['Yes'].values
x = np.arange(len(attrs))
width = 0.35
fig, ax = plt.subplots(figsize=(12, 5))
b1 = ax.bar(x - width/2, stayed_vals, width, color=COLOR_NO,  edgecolor='white', label='Stayed')
b2 = ax.bar(x + width/2, left_vals,   width, color=COLOR_YES, edgecolor='white', label='Left')
for bar, val in zip(b1, stayed_vals):
    ax.text(bar.get_x()+bar.get_width()/2, bar.get_height()+50, f'{val:,.1f}',
            ha='center', va='bottom', fontsize=9, fontweight='bold', color=COLOR_NO)
for bar, val in zip(b2, left_vals):
    ax.text(bar.get_x()+bar.get_width()/2, bar.get_height()+50, f'{val:,.1f}',
            ha='center', va='bottom', fontsize=9, fontweight='bold', color=COLOR_YES)
ax.set_title('Employee Profile: Stayed vs Left', fontsize=14, fontweight='bold', pad=12)
ax.set_xticks(x); ax.set_xticklabels(attrs, fontsize=10)
ax.set_ylabel('Value', fontsize=11); ax.legend(fontsize=10)
plt.tight_layout()
save('chart_14_stayed_vs_left.png')

# ── Chart 16: Correlation Heatmap ─────────────────────────────────────────────
print('Chart 16: Correlation Heatmap')
corr_cols = ['Age','MonthlyIncome','JobLevel','TotalWorkingYears','YearsAtCompany',
             'YearsInCurrentRole','YearsSinceLastPromotion','YearsWithCurrManager',
             'JobSatisfaction','WorkLifeBalance','AttritionBinary']
corr_labels = ['Age','Monthly\nIncome','Job\nLevel','Total Working\nYears','Years at\nCompany',
               'Years in\nCurrent Role','Years Since\nPromotion','Years with\nManager',
               'Job\nSatisfaction','Work-Life\nBalance','Attrition']
corr = df_clean[corr_cols].corr()
mask = np.triu(np.ones_like(corr, dtype=bool))
fig, ax = plt.subplots(figsize=(13, 10))
sns.heatmap(corr, annot=True, fmt='.2f', cmap='RdBu_r', center=0,
            mask=mask, ax=ax, square=True, linewidths=0.5,
            cbar_kws={'shrink': 0.75, 'label': 'Correlation'},
            xticklabels=corr_labels, yticklabels=corr_labels,
            annot_kws={'size': 8.5})
ax.set_title('Correlation Heatmap — Key Numerical Variables\n(including Attrition as binary)',
             fontsize=13, fontweight='bold', pad=15)
plt.tight_layout()
save('chart_15_correlation.png')

# ── Chart 17: Income Group Attrition ─────────────────────────────────────────
print('Chart 17: Income Group Attrition')
ig = attrition_summary(df_clean, 'IncomeGroup')
fig, ax = plt.subplots(figsize=(10, 5))
colors_ig = [COLOR_YES, '#ea580c', COLOR_NO, '#16a34a']
bars = ax.bar(ig['IncomeGroup'].astype(str), ig['Rate'], color=colors_ig, edgecolor='white', width=0.55, zorder=3)
add_bar_labels(ax, bars)
ax.axhline(AVG_LINE_RATE, color=AVG_LINE_COLOR, linestyle='--', linewidth=1.5, label=f'Avg {AVG_LINE_RATE}%')
ax.set_title('Attrition Rate by Income Group', fontsize=14, fontweight='bold', pad=12)
ax.set_xlabel('Monthly Income Group', fontsize=11); ax.set_ylabel('Attrition Rate (%)', fontsize=11)
ax.set_ylim(0, 45); ax.legend(fontsize=9)
plt.tight_layout()
save('chart_16_income_group.png')

print('\nAll charts generated successfully.')
print(f'Output directory: {OUTPUT_DIR}')
