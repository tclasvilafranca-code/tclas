import { useEffect, useState } from "react";
import type { ReactNode } from "react";
import { Link } from "react-router-dom";
import { useAuth } from "../context/AuthContext";
import { api } from "../lib/api";
import type { CategoryStat, Stats } from "../lib/api";
import { computeNextStep } from "../lib/plan";
import type { PlanIcon } from "../lib/plan";
import { BarChart, BookOpen, CheckCircle, Star, Target } from "./Icons";

const ICONS: Record<PlanIcon, (props: { className?: string }) => ReactNode> = {
  BarChart,
  BookOpen,
  CheckCircle,
  Star,
  Target,
};

export function PlanCard({ stats }: { stats: Stats | null }) {
  const { user } = useAuth();
  const [categories, setCategories] = useState<CategoryStat[] | null>(null);

  useEffect(() => {
    api
      .categoryStats()
      .then((r) => setCategories(r.categories))
      .catch(() => setCategories([]));
  }, []);

  if (!user || !stats || !categories) {
    return <div className="mt-4 h-[92px] animate-pulse rounded-2xl border border-slate-200 bg-white" />;
  }

  const plan = computeNextStep(user, stats, categories);
  const Icon = ICONS[plan.icon];

  return (
    <Link
      to={plan.href}
      state={plan.state}
      className="card-lift group relative mt-4 flex items-center gap-4 rounded-2xl border border-t48-blue/25 bg-gradient-to-br from-t48-blue/[0.06] to-transparent p-5 hover:border-t48-blue"
    >
      <div className="flex h-12 w-12 shrink-0 items-center justify-center rounded-xl bg-t48-blue text-white shadow-sm transition-transform duration-200 group-hover:scale-105">
        <Icon className="h-6 w-6" />
      </div>
      <div className="min-w-0 flex-1">
        <p className="text-xs font-bold uppercase tracking-wide text-t48-blue">Tu próximo paso</p>
        <h2 className="mt-0.5 font-extrabold text-t48-ink">{plan.title}</h2>
        <p className="mt-0.5 text-sm text-slate-500">{plan.description}</p>
      </div>
      <span className="btn-primary hidden shrink-0 px-4 py-2 text-sm sm:inline-flex">{plan.ctaLabel}</span>
    </Link>
  );
}
